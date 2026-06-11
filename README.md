# py310

## 專案說明

本專案為 Raspberry Pi GPIO 範例程式集，示範如何使用 `gpiozero` 操控 LED、PWM 呼吸燈，以及使用按鈕切換 GPIO 輸出狀態。三個範例程式對應不同硬體控制情境，適合做為入門教學與實作參考。

## 目標環境

- Raspberry Pi
- Python 3.10 以上
- Raspberry Pi OS 或相容 Linux
- `gpiozero` 套件
- `rpi-lgpio` 套件

## 依賴套件

專案使用 `pyproject.toml` 管理相依性：

- `gpiozero>=2.0.1`
- `rpi-lgpio>=0.6`

若使用 `uv` 建立虛擬環境，可依序執行：

```bash
makedir 資料夾
cd 資料夾
uv init --python 版本號
uv sync
```
```bash
啟動虛擬環境
source .venc/bin/activate
```


或直接安裝所需套件：

```bash
uv pip install gpiozero>=2.0.1 rpi-lgpio>=0.6
```

## 檔案說明

### `gpio17_led.py`

- 功能：控制 `GPIO17` 上的 LED 每秒閃爍一次。
- 行為：LED 開 1 秒、關 1 秒，無限循環，按下 `Ctrl+C` 可安全停止。
- 適用硬體：一般單色 LED + 電阻。

### `gpio23_pwm.py`

- 功能：控制 `GPIO23` 輸出 PWM 亮度，實現呼吸燈效果。
- 行為：亮度從暗到亮，再從亮到暗循環變化。
- 使用 `PWMLED`：value 範圍 0.0~1.0，對應 0%~100% 占空比。

### `gpio13_button.py`

- 功能：將 `GPIO13` 設為按鈕輸入，按下時切換 `GPIO23` 的高/低電位。
- 行為：每次按鈕觸發後，GPIO23 會在 `HIGH (ON)` 與 `LOW (OFF)` 之間切換。
- 特性：使用內建上拉電阻 (`pull_up=True`)，按鈕接地時觸發。

## 硬體接線建議

### `gpio17_led.py`

- `GPIO17` -> LED 正極
- LED 負極 -> 330Ω 電阻 -> GND

### `gpio23_pwm.py`

- `GPIO23` -> LED 正極
- LED 負極 -> 330Ω 電阻 -> GND

### `gpio13_button.py`

- `GPIO13` -> 按鈕腳位
- 另一端按鈕腳位 -> GND
- `GPIO23` -> LED 正極
- LED 負極 -> 330Ω 電阻 -> GND

> 注意：所有外部設備共用同一個接地 (GND)。若使用多個 LED 或按鈕，務必確認共地正確。

## 執行方式

### 1. LED 閃爍

```bash
python gpio17_led.py
```

### 2. PWM 呼吸燈

```bash
python gpio23_pwm.py
```

### 3. 按鈕切換輸出

```bash
python gpio13_button.py
```

## 程式設計重點

- `gpiozero` 提供簡潔的 GPIO 物件介面。
- `Button` 可搭配 `pull_up=True` 使用內部上拉電阻，減少額外硬體。
- `DigitalOutputDevice` 與 `PWMLED` 分別用於一般數位輸出與 PWM 輸出。
- 透過 `try/except/finally` 來抓取 `KeyboardInterrupt`，確保停止時釋放 GPIO 資源。

## 注意事項

- 若執行時遇到權限問題，可嘗試使用 `sudo`，但建議先確認當前使用者是否屬於 `gpio` 群組。
- 程式主要針對 Raspberry Pi GPIO 設備，若在非 Raspberry Pi 環境執行可能會失敗。
- 若要停止程式，請按 `Ctrl+C`，程式會在 `finally` 區段關閉 GPIO 裝置。

## 專案結構

- `gpio17_led.py`：LED 閃爍範例
- `gpio23_pwm.py`：PWM 呼吸燈範例
- `gpio13_button.py`：按鈕切換 GPIO23 輸出範例
- `pyproject.toml`：專案與套件相依性設定
- `README.md`：專案說明文件

