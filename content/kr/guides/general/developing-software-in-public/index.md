+++
aliases = ["/kr/5/guides/general/developing-software-in-public/", "/kr/6/guides/general/developing-software-in-public/", "/kr/7/guides/general/developing-software-in-public/", "/kr/wip/guides/general/developing-software-in-public/"]
authors = [ "brian" ]
categories = [ "Overview" ]
description = "McNeel 개발 과정 개요."
keywords = [ "developer", "rhino" ]
languages = [ "All" ]
sdk = [ "General" ]
title = "공개적인 소프트웨어 개발"
type = "guides"
weight = 0
override_last_modified = "2018-12-05T14:59:06Z"

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


## 개요

지난 20년에 걸쳐 당사는 고객께서 만족하실 수 있는 소프트웨어를 개발하기 위해 그 과정을 정립해왔습니다.   8단계로 이루어진 이 과정에서, 각 단계는 똑같이 중요합니다.   수년에 걸쳐, 당사는 이 과정의 대부분을 지원하기 위해 독자적인 도구를 구축했습니다.  하지만 이제는 상업적으로 이용 가능한 뛰어난 도구들이 있으며, 여러분께서도 직접 이 도구를 사용해보실 것을 권해 드립니다. 

당사의 소프트웨어 개발 과정은, 다른 과정들과 마찬가지로, 순환적인 사이클이어서   어디에서든 시작할 수 있습니다. 

![Rhino 개발 사이클](/images/developing-software-in-public-01.png)

## 사이클

이것은 개발자를 위한 가이드이므로, 코드 작성부터 시작해 봅시다. 

### Code (코드)

저희 개발자들이 많은 시간을 할애하는 업무입니다.   좋아하는 IDE(통합 개발 환경)를 열어 코드를 작성하고, 디버깅을 하고, 문제를 해결합니다.  저희가 아는 소프트웨어 개발자들은 모두 문제 해결하기를 즐겨하는 사람들입니다. 

뭔가 작업물이 만들어지면 이를 버전 제어 시스템에 *커밋(commit)* 합니다. 

### Commit (커밋)

저희는 [버전 제어 시스템](https://en.wikipedia.org/wiki/Version_control)에 코드를 커밋합니다.   당사의 경우, [GitHub](https://github.com/)의 [git](https://git-scm.com/)를 사용합니다.   이 외에도 많은 버전 제어 시스템이 있습니다.  과거에는 [Subversion](https://subversion.apache.org/)을 사용하였으나, 지금은 [GitHub](https://github.com/)을 사용합니다.   [GitHub](https://github.com/)은 다른 많은 도구와 원활하게 호환되며, 다양한 API를 갖췄습니다.   그 외에도  [BitBucket](https://bitbucket.org), [Mercurial](https://www.mercurial-scm.org/)를 비롯해 검토할 가치가 있는 도구들이 있습니다. 

버전 제어 시스템을 사용하지 않으셨다면, 반드시 사용하시기 바랍니다.   지금은 참 쓰기 쉬워졌습니다.   문제가 발생하기 전인 다른 버전의 소프트웨어로 되돌아갈 수 있습니다.  팀 작업에 도움이 됩니다.  버전 제어는 모든 종류의 빌드 자동화에 필요합니다.  거듭 말씀 드리지만, 정말 쉽습니다. 

개발자는 [GitHub Flow](https://guides.github.com/introduction/flow/)의 수정된 버전을 사용하여 끌어오기 요청을 만들고 마스터 브랜치에 병합합니다.

코드를 커밋한 후 빌드합니다.

### Compile (컴파일)

개발자가 책상에서 컴파일하는 작업 외에도, 코드를 지속적으로 빌드하는 전용 [TeamCity](https://www.jetbrains.com/teamcity/) 서버를 사용하여 [GitHub](https://github.com/)의 마스터 브랜치와 작동 여부를 확인합니다.   이를 통해, 상호간에 최신 코드를 얻고 컴파일하는 기능을 정상적으로 유지할 수 있습니다. 

[TeamCity](https://www.jetbrains.com/teamcity/) 서버는 모든 커밋을 검증하고, 매일 매일의 릴리스를 대부분 약 4시간마다 빌드합니다.  또한 일반에 공개되는 WIP와 서비스 릴리스도 빌드합니다. 

새 빌드가 있을 때마다 저희는 테스트를 실행합니다. 

### Test (테스트)

개발자가 버그를 수정하여 문제를 해결하면, 저희 내부 테스트 담당자가 공개 빌드가 제대로 작동하는지 확인합니다.  또한, 고객들께서도 WIP 빌드 및 릴리스 후보 빌드의 테스트에 참여해주시고 계십니다. 

테스트는 다음 과정인 공개 이전 및  이후에 실시됩니다:

### Publish (공개)

고객께 제공할 준비가 된 빌드가 있을 때마다 이를 배포(또는 공개)합니다. 

여기에는 다음의 릴리스가 포함됩니다...

- [다운로드할 수 있는 설치 프로그램](http://www.rhino3d.com/download)
- [SDK](http://developer.mcneel.com)
- 설명서

...그리고 이메일, 블로그, 소셜 미디어를 통해 일반 대중에게 공지합니다. 

### Listen (의견 수렴)

저희는 최대한 다양한 방법으로 여러분의 말씀에 귀기울입니다:

- [챗팅](http://www.rhino3d.com/support#)
- [이메일](mailto:tech@mcneel.com)
- 전화 지원, 미국 206-545-6877, 한국 02-6956-5614
- 사용자 포럼, [미국 Discourse](https://discourse.mcneel.com/), [한국 라이노스 사용자 그룹](https://rhinos.co.kr/)

그리고, 여러분의 말씀을 듣는 중에 해결해야 할 문제들을 발견하게 되는 경우가 많습니다.   때로는 작은 문제이기도 하고, 아주 큰 문제일 때도 있습니다.  저희는 항상 문제를 기록해 둡니다.

### Track (추적)

발견되는 문제들은 [YouTrack](https://mcneel.myjetbrains.com)에 기록이 됩니다. 

[YouTrack](https://mcneel.myjetbrains.com)을 통해 모든 문제를 제대로 테스트하고 확실하게 문서화할 수 있어 저희에게 큰 도움이 됩니다. 

### Prioritize (우선 순위 결정)

그 다음 중요한 것을 파악하기란 매우 어렵습니다.   저희는 고객들의 말씀을 듣고   사내에서 동료들과 서로 의견을 주고 받습니다.   Gmail, Google Drive, Google Docs로 소통하고,   24시간 열려 있는 [Slack](https://slack.com/)에서 챗팅합니다. 

매주 화요일에 미팅을 합니다.   미팅하기 전에 각자 작업 내용을 Google Doc 문서에 기입하고 공유합니다.  이 문서를 통해 다음에 출시할 제품에 대한 목표, 작업 중인 기능 그룹을 함께 공유합니다. 이 문서에는 시간 경과에 따른 진행 상황 그래프와 [YouTrack](https://mcneel.myjetbrains.com) 문제로의 링크가 있습니다. 미팅이 진행되는 동안, 각 기능의 담당 개발자가 관련 업무에 대해 직접 보고합니다. 

또한, 각 개발자는 자신의 현재 업무 내용, 다음 계획, 그리고 작업 완료에 방해가 되는 걸림돌은 무엇인지에 대해 적어 둡니다.

### 자동화

그리고 마지막으로, 많은 자동화 작업이 이루어진다는 점을 말씀 드립니다. 

다음은 자동화로 이루어지는 작업들 중 일부입니다:

- 모든 개발자의 모든 커밋을 마스터 개발 브랜치에 올리기 전에 빌드합니다.
- [TeamCity](https://www.jetbrains.com/teamcity/) 서버가 수정된 내역을 마스터 개발 브랜치에 병합하면, [YouTrack](https://mcneel.myjetbrains.com)에서 해당 문제가 종료 처리됩니다. 
- 당사의 [TeamCity](https://www.jetbrains.com/teamcity/) 서버에서 내부 및 공개 릴리스를 빌드합니다. 
- [Slack](https://slack.com/)에 명령을 입력하여 새로운 WIP 릴리스를 공개합니다. 
- 저희 다운로드 서버에 공개 릴리스를 업로드합니다. 

## 공개된 과정

최근까지 일반에 공개된 과정 중 일부는 다음과 같습니다:

- Test (테스트)
- Publish (공개)
- Listen (의견 수렴)

그리고 지난 몇 년 동안 YouTrack으로 전환하면서 이슈 추적기를 공개했습니다.  보안 또는 사용자 개인 정보 보호를 위해 일부 문제는 비공개되기도 합니다. 

가까운 시일 내에 더 많은 부분을 여러분께 공개할 수 있게 되기를 바라고 있습니다:

- 실무에서 검증된 코드 예시로 참고하실 수 있도록, 저희 코드 중 일부를 GitHub의 공개 리포지토리에 공유
- 여러분이 저희 코드를 수정 및 개선하고 이를 공유할 수 있도록 허용
- RhinoCommon을 NuGet 패키지로 공개하여 플러그인 프로젝트 빌드를 간소화
- 필요한 경우, 빌드 자동화 지원

## 관련 주제

- [Rhino 테크놀로지 개요](/guides/general/rhino-technology-overview)
- [참여](/guides/general/contributing)
- [개발자 필수 조건](/guides/general/rhino-developer-prerequisites)
