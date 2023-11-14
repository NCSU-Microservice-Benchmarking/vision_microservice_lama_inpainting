#!/usr/bin/env python3
from requests import post


# the server has an api "/tests" that accepts a get request with parameters "task", "host", "port", and "api"

if __name__ == "__main__":
    # This is based on the `flask run` output
    host = "http://127.0.0.1:5000"

    # Construct the request: {image, mask}
    image = open("test_im.png","rb").read()
    mask = open("test_mask.png","rb").read()
    files = {'image': image, 'mask': mask} 
    
    # Get the inpainted image
    print("Sending request...")
    response = post(host+"/",files=files)
    print("Received response! Status code: {response.status_code}")

    # Save the image
    if (response.ok):
        open("result.png","wb").write(response.content)
        print("Done! Check result.png")
    else:
        print("Error: faulty exit status: {response.status_code}")
