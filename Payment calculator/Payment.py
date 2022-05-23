yh = input('Enter Hours worked:')
yr = input('Enter pay rate:')
try:
	fh = float(yh)
	fr = float(yr)
except:
	print("Error, Only enter numbers please")	
	quit()

if fh > 40:
	reg = fh * fr
	otp = (fh - 40.0) * (fr * 0.5)
	yp = reg + otp
else :
	yp = fh * fr

print  ('Your pay is:', yp)
