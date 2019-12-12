#!/bin/bash


if [ `ls cropped/validation/*/*.jpg 2> /dev/null | wc -l ` -gt 0 ]; then
  echo hi
  for file in cropped/validation/*/*.jpg; do
    convert "$file" -resize 28x28\! "${file%.*}.png"
    file "$file" 
    rm "$file"
  done
fi

if [ `ls cropped/validation/*/*.png 2> /dev/null | wc -l ` -gt 0 ]; then
  echo hi
  for file in cropped/validation/*/*.png; do
    convert "$file" -resize 28x28\! "${file%.*}.png"
    file "$file" 
  done
fi

if [ `ls cropped/testing/*/*.jpg 2> /dev/null | wc -l ` -gt 0 ]; then
  echo hi
  for file in cropped/testing/*/*.jpg; do
    convert "$file" -resize 28x28\! "${file%.*}.png"
    file "$file" 
    rm "$file"
  done
fi

if [ `ls cropped/testing/*/*.png 2> /dev/null | wc -l ` -gt 0 ]; then
  echo hi
  for file in cropped/testing/*/*.png; do
    convert "$file" -resize 28x28\! "${file%.*}.png"
    file "$file" 
  done
fi

if [ `ls cropped/training/*/*.jpg 2> /dev/null | wc -l ` -gt 0 ]; then
  echo hi
  for file in cropped/training/*/*.jpg; do
    convert "$file" -resize 28x28\! "${file%.*}.png"
    file "$file" 
    rm "$file"
  done
fi

if [ `ls cropped/training/*/*.png 2> /dev/null | wc -l ` -gt 0 ]; then
  echo hi
  for file in cropped/training/*/*.png; do
    convert "$file" -resize 28x28\! "${file%.*}.png"
    file "$file" 
  done
fi
