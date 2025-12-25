# 現代化 Web UI 自動化測試專案（pytest + Playwright）

本專案提供一個以 pytest + Playwright 為核心的 Web UI 測試範本，採用 Page Object Model（POM）做物件導向設計。

## 技術組成

- 語言：Python
- 測試框架：pytest
- UI 自動化：Playwright（同步 API）
- 架構模式：Page Object Model（POM）
- 報告/輸出：pytest + Allure（產生 `allure-results`）

## 快速開始

1) 建立虛擬環境並安裝套件
```
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install
```

2) 設定目標網站（範例）
```
setx BASE_URL "https://the-internet.herokuapp.com"
setx LOGIN_USERNAME "tomsmith"
setx LOGIN_PASSWORD "SuperSecretPassword!"
setx LOGIN_INVALID_USERNAME "wrong"
setx LOGIN_INVALID_PASSWORD "wrong"
setx LOGIN_ERROR_MESSAGE "Your username is invalid!"
```

3) 執行測試
```
pytest
```

4) 產生 Allure 報告（需安裝 Allure CLI）
```
allure generate allure-results -o allure-report --clean
allure open allure-report
```

## 專案結構（OOP）

- `tests/`：測試案例（使用物件與斷言）
- `framework/pages/`：Page Objects（封裝頁面元素與操作）
- `framework/device/`：流程/用例物件（組合多個 Page Objects）
- `framework/core/`：共用基礎（瀏覽器管理、設定、BasePage）

## 設定說明（整合）

### BASE_URL 說明

`BASE_URL` 必須由你提供實際測試目標的網址，無法自動推導。建議填入可正常開啟的系統首頁或登入入口的同一個根網址，例如：

- 若登入頁是 `https://example.com/login`，則 `BASE_URL` 應設為 `https://example.com`
- 若系統用子路徑 `https://example.com/app/login`，則 `BASE_URL` 應設為 `https://example.com/app`

目前 `framework/pages/login_page.py` 預設使用 `BASE_URL + "/login"`，若你的登入頁路徑不同，請修改該檔案的 `open()` 方法。

### 目前預設的公開測試網站

本專案已預設使用 Elemental Selenium 的 The Internet 測試站：

- 網站：`https://the-internet.herokuapp.com`
- 登入頁：`https://the-internet.herokuapp.com/login`
- 預設帳號：`tomsmith`
- 預設密碼：`SuperSecretPassword!`

## 環境變數

- `BASE_URL`：目標網站根網址（預設 `https://the-internet.herokuapp.com`）
- `HEADLESS`：`1` = 無頭模式，`0` = 顯示瀏覽器
- `SLOWMO_MS`：每個動作延遲（毫秒）
- `LOGIN_USERNAME`：有效帳號
- `LOGIN_PASSWORD`：有效密碼
- `LOGIN_INVALID_USERNAME`：無效帳號（負向測試）
- `LOGIN_INVALID_PASSWORD`：無效密碼（負向測試）
- `LOGIN_ERROR_MESSAGE`：登入失敗提示文字

## 文檔與說明檔

- `modern_web_ui_pytest/README.md`：專案總覽、快速開始、架構與設定說明
- `modern_web_ui_pytest/ARCHITECTURE.md`：OOP/POM 架構說明與分層職責
- `modern_web_ui_pytest/.env.example`：環境變數範例（可複製成 `.env`）
- `modern_web_ui_pytest/pytest.ini`：pytest 規則與執行設定
- `modern_web_ui_pytest/requirements.txt`：專案依賴（含 `allure-pytest`）

## 尚需完成

- 若你要改測自己的系統，請更新 `BASE_URL`、帳號密碼，並調整 `framework/pages/*.py` 的 selector。
- 若登入頁路徑不是 `/login`，請修改 `framework/pages/login_page.py` 的 `open()`。

## 測試寫法範例（UI/E2E、BDD、壓力/效能）

以下為常見測試型態的範例寫法，作為參考與擴充方向。這些為示意，需依你的實際系統調整。

### UI/E2E（pytest + Playwright）

```python
def test_login_success(device_web):
    device_web.login("tomsmith", "SuperSecretPassword!")
    device_web.dashboard().assert_secure_area()
```

### BDD（pytest-bdd）

安裝套件：
```
pip install pytest-bdd
```

Feature 檔（`tests/features/login.feature`）：
```
Feature: Login
  Scenario: Successful login
    Given user opens login page
    When user logs in with valid credentials
    Then user should see the secure area
```

步驟定義（`tests/steps/test_login_steps.py`）：
```python
from pytest_bdd import given, when, then, scenarios
from framework.core.config import settings

scenarios("../features/login.feature")

@given("user opens login page")
def open_login(device_web):
    device_web.open_login()

@when("user logs in with valid credentials")
def do_login(device_web):
    device_web.login(settings.login_username, settings.login_password)

@then("user should see the secure area")
def assert_secure(device_web):
    device_web.dashboard().assert_secure_area()
```

### 壓力/效能（Locust）

安裝套件：
```
pip install locust
```

Locust 範例（`locustfile.py`）：
```python
from locust import HttpUser, task, between

class WebUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def login(self):
        self.client.get("/login")
        self.client.post("/authenticate", data={
            "username": "tomsmith",
            "password": "SuperSecretPassword!",
        })
```

執行：
```
locust -H https://the-internet.herokuapp.com
```
