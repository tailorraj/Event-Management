import cv2
# import numpy as np
import pyzbar.pyzbar as pyzbar
import qrcode
import Dbfun
# import matplotlib.pyplot as plt



# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr.add_data('phone number')
# qr.make(fit=True)

# img = qr.make_image(fill_color="black", back_color="white")
# img.save("sample_qr.jpg")
# image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# cv2.imwrite('sample_img.png',img)
# image = cv2.imread(img)
# print(type(img))
# decodedObjects = pyzbar.decode(image)
# print(decodedObjects)

# print(type(img))
# plt.imshow(img)
# plt.show()



# QRCode Reader
def qr_code_reader():
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_PLAIN
    data = ""

    while True:
        _, frame = cap.read()
        flag = 0

        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            
            data = obj.data.decode("utf-8")
            print(data)
            if data:
                values = data.split("&")
                if len(values) > 1:
                    res_flag = Dbfun.check_entry(str(values[0]),str(values[1]))
                    flag = 1
                    break
                else:
                    res_flag = False
                    flag = 1
                    break


        
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if flag == 1:
            return res_flag
            

# qr_code_reader()