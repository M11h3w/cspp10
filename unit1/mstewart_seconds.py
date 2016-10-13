s = input()
min = int(int(s) / 60 % 60)
sec = int(s) % 60
hr = int(float(s) / 3600)
s_s = str(s)
sec_s = str(sec)
min_s = str(min)
hr_s = str(hr)
print(s_s + " seconds is " + hr_s + " hours, " + min_s + " minute, and " + sec_s + " seconds.")