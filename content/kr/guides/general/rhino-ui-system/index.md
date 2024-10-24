+++
aliases = ["/kr/8/guides/general/rhino-ui-system/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "Rhino의 사용자 인터페이스 시스템을 간략하게 설명하는 가이드입니다."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "Rhino 사용자 인터페이스(UI) 시스템"
type = "guides"
weight = 3
override_last_modified = "2023-11-20T08:29:10Z"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"
+++

이 가이드는 Rhino의 사용자 인터페이스(UI) 시스템에 대한 간략히 설명하고, Rhino 8에 추가된 새로운 시스템을 Rhino 7 및 이전 버전과 비교합니다.

## Rhino 8 UI 시스템

새로운 Rhino 8 UI 시스템은 다음을 목표로 개발되었습니다:

- 같은 컨테이너에 표시 패널과 도구모음이 위치합니다.
- 정의를 하나의 RUI 파일에서 다른 RUI 파일로 복사하지 않고도, 여러 소스에서 도구모음과 매크로를 참조합니다.
- Rhino 또는 플러그인 서비스 릴리스에 이미 있는 파일을 덮어쓰거나 바꾸지 않고, Rhino User Interface (RUI) 변경 사항을 업데이트합니다. (이전 Rhino 버전에서는 업데이트된 도구모음과 매크로를 전달하기 위해 RUI 파일을 교체하면 사용자가 RUI 파일에 변경한 내용 위에 덮어쓰기가 되었습니다.)
- 작업 관련 도구가 표시되도록 Rhino UI를 바로바로 변경합니다.
- 사용자들 간에 UI 레이아웃을 공유합니다.
- 사용자가 UI 구성요소의 위치나 소스를 알 필요 없이 원하는 대로 UI를 수정하고, 변경 사항을 자동으로 추적할 수 있도록 허용합니다.
- Windows UI와 Mac UI를 통합시킵니다.

새로운 Rhino 8 UI 시스템의 주요 변경 사항은 다음과 같습니다:

- 컨테이너가 기존 도구모음 그룹을 대체합니다. 컨테이너는 패널과 도구모음 둘 다 표시할 수 있습니다.
- RUI 파일은 도구모음과 매크로 라이브러리를 제공하는 용도로 사용되며, 더 이상 직접 수정할 수 없습니다.  Rhino는 RUI 변경 사항을 추적하고 로드할 때 이를 적용합니다. 이를 통해 Rhino에서 사용자가 도구모음이나 매크로에 변경한 사항을 잃지 않고, RUI 파일을 업데이트할 수 있습니다. 
- 창 레이아웃이 추가되어 여러 UI 구성 간에 빠르게 전환할 수 있습니다.  창 레이아웃은 파일로 내보낼 수 있으며, 도구 모음, 매크로, 사용자 RUI 파일에 대한 수정 사항이 여기에 포함됩니다.
- 창 레이아웃을 가져오면 필요에 따라 사용자 RUI 파일이 추출되고 RUI 수정 사항이 적용됩니다. 

새로운 Rhino 8 UI 시스템은 패널, 도구모음, 매크로를 포함하여 모든 RUI 파일이나 플러그인에서 정의한 많은 소스의 UI 구성요소를 참조할 수 있도록 설계되었습니다. Rhino가 닫히면 UI의 변경 사항이 저장되고 특별히 요청하지 않는 한 원래 RUI 파일이 수정되지 않습니다. UI 레이아웃 구성은 창 레이아웃으로 저장, 복원, 내보내고 가져올 수 있으며, Windows와 Mac에서 공유가 가능합니다. 

### 컨테이너

컨테이너는 패널과 도구모음으로의 참조를 보관합니다.   도구모음은 모든 유효한 RUI 소스에서 참조될 수 있습니다.  항목은 컨테이너에서 탭으로 표시됩니다.  컨테이너는 표시하거나 숨길 수 있습니다.

탭을 한 컨테이너에서 다른 컨테이너로 끌어오거나, 컨테이너의  `톱니바퀴` 메뉴를 클릭하여 패널이나 도구모음으로의 참조를 추가 또는 제거하여 컨테이너를 수정할 수 있습니다. 같은 패널을 여러 컨테이너에서 참조할 수 있으므로, 예를 들어 `레이어` 탭을 여러 컨테이너에 표시할 수 있습니다. 

Rhino를 닫을 때 컨테이너 정의, 표시 여부, 위치, 크기가 저장되고 Rhino를 다시 시작하면 복원됩니다.  이 정보는 창 레이아웃에 저장되고 이를 통해 공유될 수 있습니다. 

컨테이너는 Rhino의 **[Containers](https://docs.mcneel.com/rhino/8/help/ko-kr/index.htm#commands/containers.htm#(null))** 명령을 사용하여 관리할 수 있습니다. 

### 창 레이아웃

창 레이아웃은 컨테이너 정의, 표시 여부 상태, 위치, 크기의 스냅샷입니다.  창 레이아웃을 복원하면 현재 UI가 재구성되어 레이아웃이 만들어졌을 때처럼 표시됩니다.  복원된 컨테이너에는 창 레이아웃이 만들어졌을 때의 순서대로 탭이 표시되며, 같은 위치와 크기로 표시됩니다.  도구모음 탭은 도구모음의 현재 정의를 참조합니다. 도구모음이 더 이상 존재하지 않으면, 탭이 표시되지 않습니다. 

창 레이아웃은 Rhino의 **[WindowLayout](https://docs.mcneel.com/rhino/8/help/ko-kr/index.htm#commands/windowlayout.htm#(null))** 명령을 사용하여 관리할 수 있습니다. 

#### 창 레이아웃 내보내기 및 가져오기

창 레이아웃은 Rhino Window Layout 파일 (RHW) 로 내보낼 수 있습니다.  내보낸 RHW 파일에는 RHW 파일이 만들어졌을 당시 모든 RUI 파일과 관련된 변경 사항과, 참조된 사용자 지정 RUI 파일이 포함됩니다.

RHW 파일을 가져오면, 내장된 사용자 지정 RUI 파일이 현재 열려 있는지 확인합니다. 해당 파일이 열려있지 않다면, 사용자 지정 파일이 추출되어 열립니다.  사용자 지정 목록이 추출되거나 확인되면, RHW 파일에 저장된 RUI 변경 사항이 현재 RUI 파일에 적용됩니다.  존재하지 않는 플러그인 파일로 정의된 도구모음과 연관된 변경 정보는 무시됩니다. 일단 RUI 데이터가 복원되면, RHW 파일에 저장된 정의와 일치하도록 컨테이너가 만들어지거나 수정됩니다. 설치되지 않은 플러그인의 도구모음만 참조하는 컨테이너는 무시됩니다.  가져온 레이아웃은 창 레이아웃 목록에 나타나며 나중에 복원할 수 있습니다. 

창 레이아웃은 Rhino의 **[WindowLayout](https://docs.mcneel.com/rhino/8/help/ko-kr/index.htm#commands/windowlayout.htm#(null))** 명령으로 내보내거나 가져올 수 있습니다. 

### RUI 파일

Rhino 8에서 이제 RUI 파일은 도구모음, 매크로, 이미지의 단순한 모음에 불과합니다.  이 파일은 컨테이너에서 참조할 수 있는 도구모음 라이브러리를 제공하기 위한 것입니다.  이제 Rhino와 플러그인 업데이트를 통해 도구모음과 매크로의 변경 사항이 제공될 수 있습니다.  업데이트된 RUI 라이브러리에 정의된 새로운 도구모음이 Toolbar 명령 목록에 자동으로 표시됩니다.  도구모음에 추가/제거된 단추는 도구모음 참조에서 추가/제거됩니다. 

RUI 파일에 정의된 도구모음 그룹은 레거시 및 플러그인 RUI 파일을 지원하기 위해 로드될 때 컨테이너로 변환되며, 플러그인 RUI 파일이 플러그인과 연관된 컨테이너를 만들 수 있게 하는 방법을 제공합니다.

링크된 RUI 파일은 Rhino의 **[옵션 > 화면표시 > 도구모음](https://docs.mcneel.com/rhino/8/help/ko-kr/index.htm#options/appearance_toolbars.htm#(null))** 옵션을 사용하여 관리할 수 있습니다. 

### 도구모음

도구모음은 단추의 모음입니다. 도구모음 단추는 모든 유효한 RUI 소스에서 올 수 있는 매크로를 참조합니다.  도구모음은 컨테이너에서 탭으로 표시됩니다. 

#### 도구모음 그룹

이제 도구모음 그룹은 처음 로드될 때 컨테이너로 변환됩니다.  이는 레거시 RUI 파일을 지원하는 용도로 존재합니다. 플러그인 개발자는 그룹을 사용하여 플러그인과 관련된 컨테이너 정의를 제공할 수도 있습니다.

#### 도구모음

도구모음은 도구모음 단추의 모음이며, 여러 컨테이너에서 참조할 수 있습니다.  다른 도구모음에서 단추를 끌어 놓거나 새 단추 마법사를 사용하여 수정할 수 있습니다.

도구모음은 Rhino의 **[Toolbar](https://docs.mcneel.com/rhino/8/help/ko-kr/index.htm#commands/toolbar.htm#(null))** 명령을 사용하여 관리할 수 있습니다.

#### 도구모음 단추

도구모음 단추는 마우스 왼쪽 및/또는 오른쪽 클릭 액션을 포함할 수 있습니다.  클릭할 때 실행하는 스크립트가 포함된 매크로에 마우스 왼쪽과 오른쪽 클릭 액션이 할당됩니다.  도구모음 단추는 마우스 왼쪽 액션에 할당된 매크로와 관련된 이미지가 있으면 표시되고, 없으면 오른쪽 클릭 매크로 이미지가 사용됩니다. 

#### 메뉴

Rhino 메뉴 시스템은 RUI 파일에 정의된 메뉴 개체를 사용하여 확장할 수 있습니다. RUI 파일에는 메뉴 시스템의 어느 위치에 항목을 삽입할지를 지정하는 위치 정보가 포함되어 있습니다. 새로운 메뉴 항목은 다음이 포함된 매크로를 참조하여 정의됩니다:

- 메뉴 텍스트.
- 메뉴 항목 이미지.
- 메뉴 항목 위에 마우스를 올리면 상태 표시줄에 표시되는 도움말 텍스트.
- 메뉴 항목을 클릭할 때 실행되는 명령 스크립트.

메뉴는 Rhino의 **[Menus](https://docs.mcneel.com/rhino/8/help/ko-kr/index.htm#toolbarsandmenus/workspace_editor.htm#(null))** 명령을 사용하여 관리할 수 있습니다. 

#### 매크로

매크로에는 매크로가 작동될 때 실행되는 명령 스크립트를 설명하는 데 필요한 정보가 포함되어 있습니다.  매크로 정의에는 다음이 포함되어 있습니다:

- 이름
- 이미지, 라이트 모드와 다크 모드 버전 모두.
- 명령 스크립트
- 단추 텍스트
- 단추 도구 설명
- 메뉴 텍스트
- 도움말 텍스트

매크로는 Rhino의 **[Macros](https://docs.mcneel.com/rhino/8/help/ko-kr/index.htm#commands/macros.htm#(null))** 명령으로 관리할 수 있습니다.

### 패널

패널은 Rhino나 플러그인이 만든 모덜리스 사용자 인터페이스 양식입니다.  패널은 모든 컨테이너에 탭으로 표시될 수 있으며, 마우스로 끌어서 놓는 방법(Drag and Drop)으로 컨테이너 간에 이동할 수 있습니다.

패널은 여러 컨테이너에서 참조될 수 있으나, 같은 컨테이너에 한 번만 표시될 수 있습니다. 

## 예전의 Rhino UI 시스템

Windows용 Rhino 7 및 그 이전 버전의 Rhino UI 시스템은 다음과 같이 구성되어 있습니다:

### 도구모음

Rhino 도구모음은 도구모음 단추의 모음입니다. 도구모음 단추는 같은 RUI 파일에 반드시 도구모음으로 정의되어 하는 매크로를 참조합니다.  단추에는 이미지, 도구 설명, 메뉴 텍스트, 도움말 텍스트, 스크립트가 포함됩니다.  도구모음 그룹에 도구모음이 표시되어 있습니다. 

### 도구모음 그룹

도구모음 그룹은 같은 RUI 파일의 도구모음에 대한 참조 모음입니다.  한 파일의 도구모음을 다른 파일에 있는 그룹으로 끌어오면, 도구모음과 참조된 매크로가 원본 파일에서 대상 파일로 복사됩니다. 도구모음 그룹은 Rhino 패널을 참조할 수 없습니다. 

### 도구모음

도구모음은 도구모음 단추의 모음이며, 도구모음 그룹에서만 참조되고 표시됩니다. 

### 도구모음 단추

도구모음 단추는 마우스 왼쪽 및/또는 오른쪽 클릭 액션을 포함할 수 있습니다. 클릭할 때 실행되는 스크립트가 포함된 매크로에 마우스 클릭 액션이 할당됩니다.  도구모음 단추는 마우스 왼쪽 액션에 할당된 매크로와 관련된 이미지가 있으면 표시되고, 없으면 오른쪽 클릭 매크로 이미지가 사용됩니다.

필요하다면, 도구모음 단추를 선택적으로 구성하여 일시적으로 다른 도구모음을 플라이아웃으로 표시할 수 있습니다.

도구모음 단추는 도구모음이 속한 동일한 RUI 파일의 매크로만 참조할 수 있습니다.  

### 메뉴

Rhino 메뉴 시스템은 RUI 파일에 정의된 메뉴 개체를 사용하여 확장할 수 있습니다.  RUI 파일에는 메뉴 시스템의 어느 위치에 항목을 삽입할지를 지정하는 위치 정보가 포함되어 있습니다.  새로운 메뉴 항목은 다음이 포함된 매크로를 참조하여 정의됩니다:

- 메뉴 텍스트.
- 메뉴 항목 이미지.
- 메뉴 항목 위에 마우스를 올리면 상태 표시줄에 표시되는 도움말 텍스트.
- 메뉴 항목을 클릭할 때 실행되는 명령 스크립트.

### 매크로

매크로에는 매크로가 작동될 때 실행되는 명령 스크립트를 설명하거나 표시하는 데 필요한 정보가 포함되어 있습니다. 매크로 정의에는 다음이 포함되어 있습니다:
참조된 도구모음 단추 또는 메뉴 항목에 표시되는 이미지.

- 단추 도구 설명.
- 단추 텍스트.
- 메뉴 항목 텍스트.
- 메뉴 항목 위에 마우스를 올리면 상태 표시줄에 표시되는 도움말 텍스트.
- 실행할 명령 스크립트.

### RUI 파일

RUI 파일은 위에 언급된 항목의 모음이며, 쓰기 가능한 디렉터리에 저장됩니다. RUI 파일에 저장된 항목은 같은 항목에 정의된 항목만 참조할 수 있습니다.  파일에 있는 항목에서 변경된 사항은 Rhino가 닫힐 때 자동으로 저장됩니다.  언제든지 RUI 파일을 열거나 닫을 수 있으며 수동으로 파일을 저장할 수 있습니다.  파일의 현재 버전이 백업되고, 변경 사항은 파일 이름에 저장됩니다.  파일이 손상된 경우 해당 파일을 삭제할 수 있으며, 이전 버전을 복원하기 위해 백업 파일의 이름을 바꿀 수 있습니다.  백업 파일이 손상되면 아무것도 복구할 수 없습니다. 

Rhino 플러그인은 플러그인과 같은 이름의 RUI 파일을 설치할 수 있으며, 해당 파일은 쓰기 가능한 위치에 복사되어 Rhino가 시작될 때 자동으로 열립니다. 플러그인은 참조될 때까지 로드되지 않아, 이를 통해 플러그인은 로드되지 않고도 Rhino 인터페이스를 확장할 수 있습니다. 

참고로, 위의 모든 기능은 Rhino 7의 **[Toobars](https://docs.mcneel.com/rhino/7/help/ko-kr/index.htm#options/toolbars.htm#(null))** 명령으로 관리할 수 있습니다. 

### Rhino 패널

Rhino 패널은 코어 Rhino 또는 플러그인이 만든 모덜리스 사용자 인터페이스 정의입니다. 

패널은 탭 모음으로 표시됩니다. 탭 모음은 패널로의 참조만 포함할 수 있으며, 패널은 단일 모음에서만 참조할 수 있습니다.  한 모음에 패널을 표시하면, 다른 모음의 해당 패널에 대한 참조가 제거됩니다. 
