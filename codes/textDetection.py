# Import required packages
import cv2
import pytesseract

def textDetection(img):
	# Homebrew is required if you want to run pytesseract on MacOS machine with m chip.
	# Mention the installed location of Tesseract-OCR in your system
	pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
	ret, thresh1 = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
	rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
	dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
	contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
													cv2.CHAIN_APPROX_NONE)
	im2 = img.copy()
	result=[]
	for cnt in contours:
		x, y, w, h = cv2.boundingRect(cnt)
		rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
		cropped = im2[y:y + h, x:x + w]
		text = pytesseract.image_to_string(cropped)
		result.append(text)
	return result