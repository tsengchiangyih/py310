"""GPIO23 PWM 呼吸燈範例。

使用 gpiozero 的 PWMLED 讓 GPIO23 輸出 PWM 訊號，
亮度會從 0% 緩慢上升到 100%，再從 100% 降回 0%，
並持續無限循環。
"""

from time import sleep

from gpiozero import PWMLED


def main() -> None:
	# 建立 PWMLED 物件並綁定到 GPIO23。
	# 在 Raspberry Pi 上，value 範圍是 0.0 ~ 1.0，分別代表 0% ~ 100% 占空比。
	led = PWMLED(23)

	# 每一步亮度變化量：0.01 代表每次增加/減少 1%。
	step = 0.01
	# 每一步之間等待 0.02 秒，數值越小變化越快。
	delay = 0.02

	try:
		# 持續循環，形成「由暗到亮，再由亮到暗」的效果。
		while True:
			# 亮度上升：i 從 0 到 100，對應 0% 到 100%。
			for i in range(0, 101):
				# i * step 會得到 0.00、0.01 ... 1.00。
				led.value = i * step
				sleep(delay)

			# 亮度下降：i 從 99 到 1，避免與上一段/下一輪重複 100% 與 0%。
			for i in range(99, 0, -1):
				led.value = i * step
				sleep(delay)
	except KeyboardInterrupt:
		# 允許使用者按下 Ctrl+C 安全停止程式。
		pass
	finally:
		# 關閉輸出並釋放 GPIO 資源，避免腳位維持在不預期狀態。
		led.off()
		led.close()


if __name__ == "__main__":
	# 直接執行此檔案時，才會進入主程式。
	main()
