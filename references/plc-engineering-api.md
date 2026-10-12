# ctrlX PLC Engineering REST API (v2): interface notes

These notes come from the spec (`plc-engineering-api-v2.json`, API 2.11.0, ctrlX WORKS 4.6.2) and were checked against a live server. Use them instead of rereading the spec. Grep the spec only for something not covered here, such as recipes, symbol config details, EPLAN or fieldbus import.

**Use `scripts/plceng.py`** for the common work: info, tree, get, push `.st`, delete, task, libraries, build, save, export and any job. The notes below cover what the script doesn't, and why it behaves as it does.

## Connecting: ask for the IP, offer the tunnel

The API is served by **ctrlX PLC Engineering on the user's (Windows) engineering PC**, not by the ctrlX CORE. Plain HTTP, no auth, port 9004 by default. The Swagger UI is at `http://<pc>:9004/?url=./plc-engineering-api-v2.json`, and the spec at `http://<pc>:9004/plc-engineering-api-v2.json`.

1. **Ask the user for the engineering PC's IP** unless they gave it in this conversation. There is no default, so don't guess or reuse an IP from memory. Then set `PLCENG_URL=<ip>` (also accepted: `<ip>:<port>` or `http://<ip>:<port>`).
2. If it can't be reached, `plceng.py` prints why and the exact tunnel command. The usual cause is the PC answering ping while port 9004 times out, because an (often IT-managed) Windows firewall drops inbound traffic. Then **offer the reverse SSH tunnel**: the PC connects out to this machine, which firewalls allow.
   ```
   ssh -N -R 9004:localhost:9004 <linux-user>@<this-machine-ip>
   ```
   The user runs it in a normal PowerShell/cmd on the engineering PC (Windows 10/11 ships `ssh`), logs in with this machine's password, and leaves the window open. It shows nothing while it works, so tell them that "it just hangs" means it's connected. Then use `PLCENG_URL=localhost:9004`. It needs an SSH server listening on this machine (`ss -ltn | grep :22`).
3. When a `localhost` URL stops answering, the tunnel window was closed. Ask the user to reopen it.
4. The calls may need the sandbox disabled (local-network or tunnel traffic).

## Base and paths

- Base: `http://<pc>:9004/plc/engineering/api/v2`
- Device tree: `/devices/{path}`. The path is element names joined by `/`, URL-encoded: `Device/Plc%20Logic/Application/PRG_Main`. On a real project it is `Device` → `Plc Logic` → `Application` (also `Realtime_Data`). The node name in job `nodeUrl`s is the same path with a `/devices/` prefix and **unencoded spaces**: `"/devices/Device/Plc Logic/Application"`.
- When names are ambiguous (a folder and a POU with the same name), address `Name.Type`, e.g. `Folder1/Test.POU`. A `.` isn't allowed in names.
- POUs view (project settings, users and groups): `/pous`, `/pous/{path}`.
- Libraries are children of `.../Application/library-manager`, **addressed by placeholder name** (`CXA_MOTION`, `CXA_PLCOPEN`), not by library name.
- Task calls appear as children `PRG_X.Unknown_TaskPOUCallObject`.

## Elements: GET / POST / PUT / DELETE /devices/{path}

GET returns `{name, elementType, id, children:[names], elementProperties:{build:{excludeFromBuild, external, enableSystemCall, linkAlways, compilerDefines}}, ...type fields}`. Code elements include their full text, so **GET is how you read code back**.

| elementType | Type fields (POST/PUT body) |
|---|---|
| `POU` | `language: "ST"`, `declaration` (header + var blocks, no `END_FUNCTION_BLOCK`), `implementation`, `level: "Standard"` |
| `POUMethod` / `POUProperty` / `POUPropertyGet` / `POUPropertySet` / `Action` | Child of the POU: POST to the POU's path. Method: `language, declaration, implementation`. Property: `declaration: "PROPERTY P : BOOL"`, then Get/Set children. Action: `implementation` only. |
| `DUT` | `declaration` (whole `TYPE … END_TYPE` with attributes), optional `textlistsupport` |
| `GVL` | `declaration` (all `VAR_GLOBAL …` blocks with attributes) |
| `PersistentVars` | `declaration` (`VAR_GLOBAL PERSISTENT RETAIN …`) |
| `ITF` / `InterfaceMethod` / `InterfaceProperty…` | `declaration` (`INTERFACE I_X`, `METHOD M …`), `displayName` |
| `Folder`, `Application` | `name`, `elementType` only |
| `Library` (POST to library-manager) | `name, version, company, placeholderName`. Find them with `GET /library-repositories/System?find=<text>`. Returns `displayName` and `resolutionInfo`. |
| `Task` (in task-config) | `priority` (string), `taskGroup`, `type:{name:"cyclic", value:"20"}`, `watchdog:{enable, time, sensitivity}`, `pouCalls:[{name, comment}]` |

- **POST** to the parent creates a child (201). A name that already exists gives **400** "An object with the name 'X' already exists within the corresponding namespace."
- **PUT** on the element updates it in place (200), e.g. new declaration/implementation. This is better than delete+create because it keeps the object id.
- **DELETE** removes the element and its children (200). Missing elements give **404** "Path '/…' not found in project."
- **PATCH** (`application/merge-patch+json`) on a Device: `{"disable": bool}`, `{"plcSettings": {...}}`. On a library: `{"parameters":[{name,value}]}`.

### Quirks found on the live server

- **PUT on a task APPENDS `pouCalls`**; it doesn't replace them. To set the list, PUT with `"pouCalls": []` first, then PUT the wanted list. `plceng.py task` does this.
- **A task call object can't be deleted**: DELETE `.../MainTask/PRG_X.Unknown_TaskPOUCallObject` gives 501 "Not yet implemented". Use the empty-list PUT.
- A deleted program stays in `pouCalls` and breaks the build ("Identifier 'PRG_X' not defined, Object: MainTask"). Fix the task when you replace programs.
- `BuildJob` action: the spec's enum says `GenerateCodeJob`, but the example and the live server use **`"GenerateCode"`**, which works.
- The build result gives the error **text** for errors, but only a **count** for warnings. Ask the user to look at warnings in the IDE's message view.
- **Ladder (LD) can't go through the API.** POST of a POU with `"language":"LD"` gives 400 "Language type 'LD' is not supported", even though the spec's `Language` enum lists LD (and FBD, CFC, SFC, IL). Only ST is accepted. **If the project has any ladder, the whole project goes in as one PLCopenXML.** Don't push the ST parts separately. Compile every object (ST and ladder) with `st_to_plcopenxml.py` into one file, as before, and load it with `plceng.py import-xml <file.xml>`, which picks the route:
  1. **PLC Engineering runs on this machine** (the open project's file is visible here; a localhost URL through the SSH tunnel does NOT count): the import job reads the local file directly.
  2. **The user provides a shared folder** both machines can reach: `import-xml <file.xml> --shared <local-dir> <pc-dir>` copies the file there and imports it from the PC's path for it.
  3. **Otherwise, prompt the user to load the export by hand** (Project → Import PLCopenXML…) and wait for them to confirm. Then run `plceng.py build` and fix the errors. `import-xml` exits with code 3 and says so.
  `plceng.py push` refuses a file set that contains ladder (exit 4).
- **`ImportPlcOpenXmlJob` reads the file from the engineering PC's disk** (`filePath` is a Windows directory there), and so do export, import, project open and save-as. There's no upload endpoint. From another machine, push `.st` objects with POST/PUT instead (`plceng.py push`), or have the user copy the XML to the PC.

## Errors

Problem JSON: `{severity, type, title, status, detail, mainDiagnosisCode, detailedDiagnosisCode, dynamicDescription}`. **`dynamicDescription` holds the useful text.** Status codes: 400 BadRequest, 403, 404 NotFound, 500, 501 NotImplemented.

## Jobs: POST /jobs, then poll GET /jobs/{id}

Body: `{"jobType": "...", "jobParameters": {...}}`. The response and poll result are `{id, state: Pending|Running|Done|Failed, progress, jobType, jobParameters, jobResultInfo}`. **`jobResultInfo`** holds the result. Build messages are joined with `" | "`. `GET /jobs` lists recent jobs.

| jobType | jobParameters (example) | Notes |
|---|---|---|
| `BuildJob` | `{"action":"GenerateCode"}` | Builds the active app. "Build complete -- N errors, M warnings: Ready for download." State is `Failed` when there are errors. |
| `ProjectJob` | `{"action":"Save"}`; save-as: `{"action":"Save","path":"D:\\x.project"}`; `{"action":"Open","path":…,"keepProjectVersion":false,"projectEnvironment":"SetAllToNewest"}`; `{"action":"Close"}`; `SaveAndInstallIntoLibraryRepository`; `{"action":"SaveAsCompiledLibrary","path":…}` | Changes made over the API aren't on disk until Save. |
| `NewProjectJob` | `{"filePath":"D:\\test","fileName":"untitled1","template":"ctrlXOSx64"}` | Templates: `EmptyProject, EmptyLibrary, StandardLibrary, ctrlXOSARM64, ctrlXOSx64` |
| `ImportPlcOpenXmlJob` | `{"nodeUrl":"/devices/Device/Plc Logic/Application","filePath":"D:\\dir","fileName":"x.xml"}` | File on the PC. Existing objects are overwritten. |
| `ExportPlcOpenXmlJob` | same keys, `nodeUrl` = the element to export | Writes on the PC. Good for a backup before deleting code. |
| `ImportJob` / `ExportJob` | native `.export`. Export also takes `oneFilePerSubtree`, `includeSubNodes`. | |
| `ApplicationLoginJob` | `{"nodeUrl":"/devices/Device/PLC Logic/Application","loginOption":"LoginWithOnlineChange"\|"LoginWithDownload"\|"LoginWithoutAnyChange","updateBootApplication":true}` | **Downloads to the real controller.** Confirm with the user first. |
| `ApplicationJob` | `{"action":"Start"\|"Stop"\|"Logout","nodeUrl":…}` | Starts or stops the PLC program on the controller. Confirm first. |
| `ResetApplicationJob` | `{"action":"ResetWarm"\|"ResetCold"\|"ResetOrigin"}` | Confirm first. |
| `CommunicationSettingsJob` | `{"nodeUrl":"/devices/Device","ipAddress":"…","httpsPort":443,"plcPort":11740}` | Sets the target controller address. |
| `DeviceUserLoginJob` / `DeviceUserLogoutJob` | `{"nodeUrl":"/devices/Device","username":…,"password":…}` | Device user management on the controller. |
| `UserManagementLogInJob` / `LogOutJob` | `{"userName":"Owner","password":""}` | Project user management. |
| `FindElementsJob` | `{"nodeUrl":…,"findText":"x","matchCase":false,"matchWholeWord":false,"searchOptions":"NodeAndSubNodes"}` | |
| `MoveElementsJob` | `{"sourceNodeUrl":…,"destinationNodeUrl":…}` | |
| `OpenEditorJob` | `{"nodeUrl":…}` | Opens the editor in the IDE. `GET /editors` and `/editors/active` list them. |
| `PreCompileJob` | `{"action":"Enable"\|"Disable"}` | |
| `DeclarationsJob` | `{"nodeUrl":".../PersistentVars","action":"AddAllInstancePaths"}` | |
| `PubSubJob` | `{"nodeUrl":".../GVL","action":"SetAsPublisher"\|"SetAsSubscriber"}` | |
| `PublishMarkedMethodsJob` | `{"nodeUrl":".../symbol-config"}` | |
| `ImportFieldbusConfigJob` | `{"nodeUrl":"/devices/device/Realtime_Data","username":…,"password":…,"busType":"Ethercat","forceInsert":true}` | Reads the bus config from the controller. Offline variant: `ImportOfflineFieldbusConfigJob` with `filePath`, `fileName`, `keepExisting`. |
| `EplanJob`, `LibraryCategoriesJob`, `DeviceRepositoryJob`, `Import/ExportUsersAndGroupsJob` | see the spec examples (`components.examples.*Request`) | |

## Other endpoints

- `GET /product/info` → `{"versionText":"4.6.2"}`
- `GET /projects/current[?option=extended]` → name, path, times, `profileName`, `compilerVersion`. `extended` adds `elementList` (top-level nodes).
- `GET|PUT|DELETE /devices/{app}/task-config[/{task}]`. `PUT task-config?taskGroupsAction=…` handles task groups (`taskGroups:[{groupName, core}]`).
- `GET|PUT /devices/{app}/symbol-config` takes query `showProjSymbols, showLibSymbols, showExpAttrSymbols, includeMaxAccessNone, includeAllTypes`. PUT takes `symbolsAction` and a body with `symbols:[{name, isSelected, variables:[{name, accessRights, isSelected}]}]`, plus `supportOPCUA`, `optimizedLayout` and `includeCommentsInXML`.
- Recipes: `/devices/{path}/recipe-manager/{def}/variables[/{name}]` and `/recipes[/{name}]`.
- `/library-repositories[/{repo}[/{libDisplayName}]]` and `/device-repositories/...` install and uninstall libraries or devices in the repository. That's different from adding a library to a project.
- `/online-change-memory-reserve[/{app}]` handles the memory reserve per FB.
- `/pous/project-settings/users-groups/user|group/{name}` handles project users and groups.

## Safe workflow for replacing code

1. `plceng.py info`: confirm it's the right project.
2. Back up: `plceng.py export-xml "Device/Plc Logic/Application" "<dir on the PC>" <name>_backup_<date>.xml`, in the project's folder (taken from `info`).
3. `plceng.py push src/*.st --dry-run`, then without `--dry-run`. Add `--prune` only when the user asked to remove the old code; it deletes POU/DUT/GVL/ITF objects not in the files.
4. `plceng.py lib-add <name>` for each library the code needs. Match versions to the libraries already there (e.g. CXA_Motion 4.6.2.0 → CXA_PLCopen 4.6.2.0).
5. `plceng.py task MainTask PRG_X` when the programs changed.
6. `plceng.py build`. Fix the errors and repeat.
7. `plceng.py save` only when the user asks. Login, download and start are separate, explicit steps.
