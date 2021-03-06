

from PIL import Image
import numpy as np
import cv2
# import streamlit as st
import time
import math
from multiprocessing import Process, cpu_count
import glob
import sys, os

# to make sure even image sizes for merging and blending operations

im1 = cv2.imread("option_1/landscape1.jpg")
im2 = cv2.imread("option_1/landscape2.jpg")

print(im1.shape, im2.shape)

im1 = cv2.resize(im1, (640, 480))
im2 = cv2.resize(im2, (640, 480))

cv2.imwrite("option_1/landscape1.jpg", im1)
cv2.imwrite('option_1/landscape2.jpg', im2)

def option1(option='d'):

    if not os.path.exists('option1'):
      os.mkdir('option1')

    start_t1 = time.time()
    im1 = Image.open("option_1/landscape1.jpg")
    im2 = Image.open("option_1/landscape2.jpg")
    
    im3 = Image.blend(im1, im2, 0.5)
    end_t1 = time.time()
    im3.save("option1/Blended.jpg")

    # -------------------------------------------------- #

    img = cv2.imread("option1/Blended.jpg", cv2.IMREAD_GRAYSCALE)
    start_t2 = time.time()
    rows, cols = img.shape

    # Vertical wave
    if (option == 'a'):
        img_output = np.zeros(img.shape, dtype=img.dtype)
        for a in range(5):
            for i in range(rows):
                for j in range(cols):
                    offset_x = int(25.0 * math.sin(2 * 3.14 * i / 180))
                    offset_y = 0
                    if j + offset_x < rows:
                        img_output[i, j] = img[i, (j + offset_x) % cols]
                    else:
                        img_output[i, j] = 0

    # Horizontal wave
    elif option == 'b':
        img_output = np.zeros(img.shape, dtype=img.dtype)
        for a in range(5):
            for i in range(rows):
                for j in range(cols):
                    offset_x = 0
                    offset_y = int(16.0 * math.sin(2 * 3.14 * j / 150))
                    if i + offset_y < rows:
                        img_output[i, j] = img[(i + offset_y) % rows, j]
                    else:
                        img_output[i, j] = 0

    # Concave effect
    elif (option == 'c'):
        img_output = np.zeros(img.shape, dtype=img.dtype)
        for a in range(5):
            for i in range(rows):
                for j in range(cols):
                    offset_x = int(350.0 * math.sin(2 * 3.14 * i / (2 * cols)))
                    offset_y = 0
                    if j + offset_x < cols:
                        img_output[i, j] = img[i, (j + offset_x) % cols]
                    else:
                        img_output[i, j] = 0

    # Both horizontal and vertical
    if (option == 'd'):
        img_output = np.zeros(img.shape, dtype=img.dtype)
        for a in range(5):
            for i in range(rows):
                for j in range(cols):
                    offset_x = int(20.0 * math.sin(2 * 3.14 * i / 150))
                    offset_y = int(20.0 * math.cos(2 * 3.14 * j / 150))
                    if i + offset_y < rows and j + offset_x < cols:
                        img_output[i, j] = img[(i + offset_y) % rows, (j + offset_x) % cols]
                    else:
                        img_output[i, j] = 0

    end_t2 = time.time()
    time_taken = (end_t1 - start_t1) + (end_t2 - start_t2)
    cv2.imwrite('option1/Input.jpg', img)
    cv2.imwrite('option1/BNWOutput.jpg', img_output)

    return time_taken

# option1()

def option2():
    if not os.path.exists('option2'):
      os.mkdir('option2')

    # st.header("Edge Detection Test")

    start_time = time.time()
    # Read image from disk.
    path = 'option_1/'
    files = os.listdir(path)

    i = 0
    count = 0
    X_data = []
    for myFile in files:
      try:
        image = cv2.imread(path + myFile)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        X_data.append(image)
        edges = cv2.Canny(image, 100, 200)
        cv2.imwrite('option2/image-{}.jpg'.format(i), edges)
        i += 1
      except:
        pass

    incr_time = time.time() - start_time
    i = i + 1
    count += 1
    end_time = time.time()
    """for i in range(count):
        st.image(X_data[i], width=800)
    st.image('image-{}.jpg'.format(i), width=800)"""
    time_taken = end_time - start_time
    # st.subheader("Time taken to run Edge Detection Test is " + str("%.3f" % time_taken) + " seconds")
    return time_taken

# option2()

def option3():
    # st.header("Gaussian Blur Test")

    if not os.path.exists('option3'):
      os.mkdir('option3')

    start_time = time.time()
    img = cv2.imread('option_1/landscape1.jpg')
    blur = cv2.GaussianBlur(img, (7, 7), 0)
    for i in range(10):
        blur = cv2.GaussianBlur(blur, (7, 7), 0)
    end_time = time.time()
    time_taken = end_time - start_time
    # st.markdown('<style>body{background-color: Black;}</style>',unsafe_allow_html=True)
    # st.image(img, width=800, caption='Original Image')
    # st.image(blur, width=800, caption='Blurred Image')
    cv2.imwrite('option3/gaussian_blur.jpg', blur)
    # st.subheader("Time taken to run Gaussian Blur Test is " + str("%.3f" % time_taken) + " seconds")
    return time_taken

# option3()

def option4():
    # st.header("Erosion & Dilation Test")
    if not os.path.exists('option4'):
      os.mkdir('option4')

    start_time = time.time()
    img = cv2.imread('option_1/landscape1.jpg', 0)
    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((5, 5), np.uint8)
    # The first parameter is the original image,
    # kernel is the matrix with which image is
    # convolved and third parameter is the number
    # of iterations, which will determine how much
    # you want to erode/dilate a given image.
    
    img_erosion = cv2.erode(img, kernel, iterations=4)
    img_dilation = cv2.dilate(img, kernel, iterations=4)
    end_time = time.time()
    time_taken = end_time - start_time
    cv2.imwrite('option4/Erosion.jpg', img_erosion)
    cv2.imwrite('option4/Dilation.jpg', img_dilation)

    """st.image(img, width=800, caption="Original Image")
    st.image(img_erosion, width=800, caption="Eroded Image")
    st.image(img_dilation, width=800, caption="Dilated Image")
    st.subheader("Time taken to run Erosion & Dilation Test is " + str("%.3f" % time_taken) + " seconds")"""

    return time_taken
  
# option4()

#matrix multiplication test
def matrixMult():
    start_time = time.time()
    X = []
    result = []
    for i in range(4):
        a = []
        b = []
        for j in range(4):
            a.append(int(j + 1))
        b.append(int(0))
        X.append(a)
        result.append(a)
  
    for i in range(len(X)):
        for j in range(len(X[0])):
            for k in range(len(X)):
                result[i][j] += X[i][k] * X[k][j]

    end_time = time.time()
    time_taken = end_time - start_time
    # st.subheader("Time taken to run Matrix Multiplication Test is " + str("%.3f" % time_taken) + " seconds")
    return time_taken

# matrixMult()

def option5(choice='b', PROCESSES=2):
    # st.header("Matrix Multiplication Tests")

    start_time = time.time()

    if (choice == 'a'):
        for i in range(8):
            matrixMult()
        return time.time() - start_time

    elif (choice == 'b'):
        start_t = time.time()
        A = list()

        if __name__ == "__main__":
            for i in range(PROCESSES):
                A.append(Process(target=matrixMult))
                A[i].start()
                for i in A:
                    i.join()

            dt = time.time() - start_t
            end_time = time.time()
            time_taken = end_time - start_time
            # st.subheader("Time taken to run Matrix Multiplication Test is " + str("%.3f" % time_taken) + " seconds")
            return time_taken

# option5('a')

#factorial test
def option6():
    # st.header("Factorial Tests")
    start_time = time.time()
    fact = [1 for i in range(7000)]
    a = [i for i in range(7000)]

    for i in range(7000):
        for j in range(1, a[i] + 1):
            fact[i] = fact[i] * j
    time_taken = time.time() - start_time
    # st.subheader("Time taken to run Factorial Test is " + str("%.3f" % time_taken) + " seconds")
    return time_taken

# option6()

if __name__ == "__main__":
    # st.title("RA\u00b2 Benchmark")
    print("\nDo you want to run a custom benchmark?\n")
    print("Note that typing in 'no' will let you run a default benchmark\n")
    print("Typing 'yes' will let you choose the tests you want to run individually\n")
    run_choice = input("Enter your choice: ")
    if (run_choice == 'yes'):
        time_taken = 0
        while (1):
            print(
                "\nMenu:\n1. Blend and warp\n2. Edge detection\n3. Gaussian Blur\n4. Erosion & Dilation\n5. Matrix Multiplication\n6. Factorial\n7. Exit")
            a = int(input("\nEnter choice: "))
            if (a == 1):
                print("\na. Vertical\nb. Horizontal\nc. Concave\nd. Multidirectional\n")
                opt = input("Enter choice: ")
                print("\nTime taken for blend & warp test is %.3f seconds" % option1(opt))
            elif (a == 2):
              print("Time taken for edge detection test is %.3f seconds" % option2())
            elif (a == 3):
              print("Time taken to perform Gaussian Blur test is %.3f seconds" % option3())
            elif (a == 4):
              print("Time taken to perform Dilation & Erosion test is %.3f seconds" % option4())
            elif (a == 5):
              print("\na. Single core\nb. Multi core")
              opt = input("\nEnter choice: ")
              if opt == 'b':
                  ch = input("\ni. Default (number of logical cores)\nii. Custom\n\nEnter choice: ")
                  if (ch == 'i'):
                      print("\nTime taken to create and execute %d processes using multiprocessing is %.3f seconds" % (
                          cpu_count(), option5(opt)))
                  if (ch == 'ii'):
                      thr = int(input("Enter number of processes: "))
                      print("\nTime taken to create and execute %d processes using multiprocessing is %.3f seconds" % (thr, option5(opt, thr)))
              else:
                print("\nTime taken to multiply the matrices 8 times using a single core is %.3f seconds" % option5(opt))
            elif (a == 6):
              print("Time taken to perform factorial test is %.3f seconds" % option6())
            elif (a == 7):
              sys.exit(0)
    elif (run_choice == 'no'):
      run_1 = option1()
      print("\nTime taken for blend & warp test is %.3f seconds" % run_1)
      run_2 = option2()
      print("\nTime taken for edge detection test is %.3f seconds" % run_2)
      run_3 = option3()
      print("\nTime taken to perform Gaussian Blur test is %.3f seconds" % run_3)
      run_4 = option4()
      print("\nTime taken to perform Dilation & Erosion test is %.3f seconds" % run_4)
      run_5 = option5()
      print("\nTime taken to execute %d processes performing matrix multiplication using multiprocessing is %.3f seconds" % (cpu_count(), run_5))
      run_6 = option6()
      print("\nTime taken to perform factorial test is %.3f seconds" % run_6)
      print("\nTotal time taken to run the benchmark is %.3f seconds" % (run_1 + run_2 + run_3 + run_4 + run_5 + run_6))
      # st.header("Total time taken to run the benchmark is " + str("%.3f" % (run_1 + run_2 + run_3 + run_4 + run_5 + run_6)) + " seconds")

























