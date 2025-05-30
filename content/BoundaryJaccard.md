Title: Boundary Jaccard Metric
Date: 2020-10-25 09:30
Category: Python
Tags: metrics, image processing
Slug: boundary-jaccard
Authors: Peter Mortimer
Summary: Visualizing the Boundary Jaccard metric for Semantic Image Segmentation.
Tocify: True
Status: draft

<h1 style="visibility:hidden;">Boundary Jaccard (BJ Metric)</h1>

The recently introduced Boundary Jaccard [[1](#bj_iv)] metric is a new evaluation metric for semantic segmentation algorithms. The BJ lays a focus on the segmentation accuracy along the contours. Describing this mathematically can be a bit awkward. Luckly, visualizing the regions of interest of the BJ metric can provide a more intuitive understanding of its caluclation. 

I'll quickly introduce the use case in which we will analyze the BJ metric. The Cityscapes dataset [[2](#cityscapes)] is a large-scale dataset consisting of urban driving scenes recorded across many German cities with high quality pixel-level annotations. Cityscapes is a commonly used dataset for the development of semantic image segmentation methods. We will use Fast-SCNN [[3](#fast_scnn)] as our semantic segmentation algorithm, since it produces fairly reasonable predictions on the Cityscapes dataset. 

<hr>
<div class="row">
<div class="col-4 col-sm-4">
<a href="/images/bj_metric/darmstadt_anon.png" 
data-lightbox="cityscapes-darmstadt" 
data-title="This is an input out of the training set of the Cityscapes dataset." 
data-alt="This is an input out of the training set of the Cityscapes dataset."><img src="/images/bj_metric/darmstadt_anon.png"></a>
</div>
<div class="col-4 col-sm-4">
<a href="/images/bj_metric/darmstadt_gt.png" 
data-lightbox="cityscapes-darmstadt" 
data-title="This is a ground truth annotation out of the Cityscapes dataset. Each color represents a different semantic class." 
data-alt="This is a ground truth annotation out of the Cityscapes dataset. Each color represents a different semantic class."><img src="/images/bj_metric/darmstadt_gt.png"></a>
</div>
<div class="col-4 col-sm-4">
<a href="/images/bj_metric/darmstadt_pred.png" 
data-lightbox="cityscapes-darmstadt" 
data-title="This is an example prediction of the Fast-SCNN network. Notice how the car hood is falsely predicted as part of the road surface. The BJ metric is a method to quantitatively evaluate the accuracy of a semantic scene segmentation." 
data-alt=""><img src="/images/bj_metric/darmstadt_pred.png"></a>
</div>
</div>

<span class="caption">Here is an example scene out of the Cityscapes dataset. The second column shows the ground truth scene annotation by a human. The third column shows the output prediction of the Fast-SCNN network on the same input image. The question is how can we evaluate the model prediction in a quantitative manner?</span>
<hr>

### Introducing the BJ Metric

Metrics for the semantic scene segmentation are calculated for each class $c$ of a segmentation map $S$. We denote the pixels of a segmentation map that belong to class $c$ as $S^{c}$. Here we also distinguish between the predicted segmentation map $S_{ps}$ and the ground truth segmentation map $S_{gt}$.

The authors of the BJ metric are inspired by the so-called BF [[4](#bf_bmvc)] score ("Boundary F1 score"). The BF score introduces the notion of focusing on the segmentation accuracy along class borders, since this is where a good semantic segmentation can still make most of its mistakes. For this we define $B^{c}$ as the pixels along the border of a class $c$ and $[[\cdot]]$ denotes the Iversons bracket notation, where $[[z]] = 1$ if $z=true$ and $0$ otherwise.

$$ P^{c} = \frac{1}{|B_{ps}^{c}|} = \sum_{x \in B_{ps}^{c}} [[d(x,B_{gt}^{c}) < \theta ]]$$

$$ R^{c} = \frac{1}{|B_{gt}^{c}|} = \sum_{x \in B_{gt}^{c}} [[d(x,B_{ps}^{c}) < \theta ]]$$

$$ BF^{c} = F_{1}^{c} = \frac{2 \cdot P^{c} \cdot R^{c}}{P^{c} + R^{c}}$$

This assumption on the higher relevance along the class borders is combined with the common Jaccard index (a.k.a. Intersection over Union). The Jaccard index is an established evaluation metric for 2D and 3D object detection tasks and can also be used to evaluate 2D semantic maps. In simple terms, the Jaccard index looks at the size of the relative overlap between the area made up by the prediction pixels and the ground truth pixels.

$$ IoU^{c} = \frac{S_{ps}^{c} \cap S_{gt}^{c}}{S_{ps}^{c} \cup S_{gt}^{c}} $$

### References

<span id='bj_iv'>[1] Eduardo Fernandez-Moral, Renato Martins, Denis Wolf, Patrick Rives (IV 2018) [A new metric for evaluating semantic segmentation: leveraging global and contour accuracy](https://hal.inria.fr/hal-01581525/document).</span>

<span id='cityscapes'>[2] Marius Cordts, Mohamed Omran, Sebastian Ramos, Timo Rehfeld,
Markus Enzweiler, Rodrigo Benenson, Uwe Franke, Stefan Roth, Bernt Schiele (CVPR 2016) [The Cityscapes Dataset for Semantic Urban Scene Understanding](https://www.cityscapes-dataset.com/wordpress/wp-content/papercite-data/pdf/cordts2016cityscapes.pdf).</span>

<span id='fast_scnn'>[3] Rudra P. K. Poudel, Stephan Liwicki, Roberto Cipolla (BMVC 2019) [Fast-SCNN: Fast Semantic Segmentation Network](https://bmvc2019.org/wp-content/uploads/papers/0959-paper.pdf) - I use the [PyTorch implementation of Fast-SCNN](https://github.com/Tramac/Fast-SCNN-pytorch) by the GitHub User Tramac.</span>

<span id='bf_bmvc'>[4] Gabriela Csurka, Diane Larlus, Florent Perronnin (BMVC 2013) [What is a good evaluation measure for semantic segmentation?](http://www.bmva.org/bmvc/2013/Papers/paper0032/paper0032.pdf)</span>