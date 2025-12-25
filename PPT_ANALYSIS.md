# Pytest 訓練 PPT - Python 內容摘要

本文整理 `pytest` 訓練 PPT 中與 Python 相關的內容，並指出最可能使用的測試框架。已依照需求忽略 TR-069/USP 的 REST/JSON 與 Allure JSON 顯示重點。

## Python 知識涵蓋

- 安裝與入門（Windows 下載、Hello World、基本執行）。
- 語法基礎：縮排、變數、型別轉換、輸出。
- 作用域：區域/全域變數、`global` 關鍵字、跨檔變數存取注意事項。
- 資料型別重點：tuple（建立、索引、切片、解包、list 互轉、迭代、串接）。
- 流程控制：`if/elif/else`、邏輯運算、`pass`、`while`/`for`、`break`、`continue`、`range`。
- 函式：定義、參數、引數、基本範例。

## 最可能使用的測試框架

- 主要是 `pytest`，PPT 反覆說明 pytest 結構、命名規範、setup/teardown 與層級設計，並搭配 Allure 產生報告。
