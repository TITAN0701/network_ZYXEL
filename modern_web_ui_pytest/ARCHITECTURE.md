# 架構說明

此專案以 pytest 作為測試框架、Playwright 作為 Web UI 自動化引擎，採用物件導向的 Page Object Model（POM）。

## 物件導向設計

```
Tests (tests/)
  ↓
Use-case/Flow Objects (framework/device/)
  ↓
Page Objects (framework/pages/)
  ↓
Core 基礎 (framework/core/)
```

### Tests
- 負責測試情境與斷言，保持可讀性與可維護性。
- 透過高層物件呼叫，避免直接操作 selector。

### Use-case/Flow Objects
- 封裝跨頁流程，例如登入、設定、導覽等高層操作。
- 組合多個 Page Object，提供清楚的商務語意。

### Page Objects
- 實作頁面上的實際操作與 selector。
- 每個頁面對應一個 class，維持低耦合。

### Core 基礎
- 瀏覽器啟動/關閉、共用設定、BasePage 等基礎能力。

## 建議的物件導向框架

- 建議採用 Page Object Model（POM）。它能將 UI 操作與測試邏輯分離，適合中大型 Web UI 測試，且與 pytest + Playwright 搭配成熟。
