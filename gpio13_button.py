"""GPIO13 按鈕切換 GPIO23 輸出狀態。

需求：
- GPIO13 作為按鈕輸入。
- 每按一下，GPIO23 在高電位/低電位之間切換一次。
- 重複按壓時持續循環切換。
"""

from signal import pause

from gpiozero import Button, LED


def main() -> None:
	# GPIO13 設為按鈕輸入。
	# pull_up=True 代表使用內建上拉：
	# 未按下時為高電位，按下（接地）時為低電位，屬於 active-low 設計。
	button = Button(13, pull_up=True, bounce_time=0.05)

	# GPIO23 設為 LED 輸出，初始為低電位（關閉）。
	output = LED(23)
	output.off()

	def toggle_output() -> None:
		# 每次按下按鈕就反轉目前輸出狀態：
		# False -> True（低 -> 高），True -> False（高 -> 低）。
		output.value = not output.value
		state_text = "高電位 (ON)" if output.value else "低電位 (OFF)"
		print(f"GPIO23 已切換為：{state_text}")

	# 綁定事件：按下時執行切換。
	button.when_pressed = toggle_output

	try:
		print("程式啟動：按下 GPIO13 按鈕可切換 GPIO23 高/低電位。")
		print("按 Ctrl+C 結束程式。")
		# 讓事件回呼持續運作，不讓主程式提前結束。
		pause()
	except KeyboardInterrupt:
		pass
	finally:
		# 結束前關閉輸出並釋放 GPIO 資源。
		output.off()
		output.close()
		button.close()


if __name__ == "__main__":
	main()
