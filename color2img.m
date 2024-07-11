% To Read a color image from user
img = imread('imagep.jpg'); 

% Convert to grayscale by using built in fun
gray_img = rgb2gray(img);

% it Display original and grayscale images
figure;
subplot(1, 2, 1);
imshow(img);
title('Original Image');

subplot(1, 2, 2);
imshow(gray_img);
title('Grayscale Image');
