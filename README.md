# CVFX-HW5
Scores
(5%) Take multi-view images by yourselves
(5%) Show image alignment results between different images
(20%) Generate the multi-view 3D visual effects
(10%) Exploit creativity to add some image processing to enhance effect (Using post-production software is allowed)
(10%) Bonus - Complete the above 3 different effects
(30%) Assistant score
(20%) Mutual evaluation
Motion parallax
## 1.Take multi-view images by myself
|              |Image1|Image2|Image3|Image4|Image5|
|--------------|------|------|------|------|------|
|**Example 1**|<img width="125" height="125" src='src/tt1.jpg'>|<img width="125" height="125" src='src/tt2.jpg'>|<img width="125" height="125" src='src/tt3.jpg'>|<img width="125" height="125" src='src/tt4.jpg'>|<img width="125" height="125" src='src/tt5.jpg'>
|**Example 2**|<img width="125" height="125" src='src/gg1.jpg'>|<img width="125" height="125" src='src/gg2.jpg'>|<img width="125" height="125" src='src/gg3.jpg'>|<img width="125" height="125" src='src/gg4.jpg'>|
|**Example 3**|<img width="125" height="125" src='src/IMG_0065.JPG'>|<img width="125" height="125" src='src/IMG_0066.JPG'>|

## 2.image alignment results
In our homework, we use the center image of captured order as basline. In term of, the other images all need to align with the image whose captured order was middle. <br>
Here show the alignment results of Example 1 

|All align with Image3<br>(center image)|**Example 1**|
|:-------------------:|-------------|
|Image1|<img src='matching_fig/matching1.jpg'>|
|Image2|<img src='matching_fig/matching2.jpg'>|
|Image3|<img src='matching_fig/matching3.jpg'>|
|Image4|<img src='matching_fig/matching4.jpg'>|
|Image5|<img src='matching_fig/matching5.jpg'>|

## 3.Generate the multi-view 3D visual effects
We do some examples in motion parallex. Here show the results.

|             |**GIF Result**|
|:-----------:|--------------|
|**Example 1**|<img src='ttt.gif'>|
|**Example 2**|<img src='ggg.gif'>|
|**Example 3**|<img src='aaa.gif'>|
|**Example 4**|<img src='result_1.gif'>|
|**Example 5**|<img src='result_2.gif'>|

As you can see, Example 2 seems perform not good. The reason we think is that Example 2 contain fewer feature.
Also, we compare the reulsts of using different number of images. The ablation study will show below.

|Five Images|Four Images|
|--------------------|----------------------|
|<img src='ttt.gif'>|<img src='ttt1.gif'>|

|Three Images|Two Images|
|--------------------|----------------------|
|<img src='ttt2.gif'>|<img src='ttt3.gif'>|

We can see that the more images we use, the more obvious sourrending effect we can see.

## 4.Exploit creativity to add some image processing to enhance effect (PhotoShop)
