Title: Boundary Jaccard Metric
Date: 2020-10-25 09:30
Category: Python
Tags: metrics, image processing
Slug: boundary-jaccard
Authors: Peter Mortimer
Summary: Visualizing the Boundary Jaccard metric for Semantic Image Segmentation.
Tocify: True
<!--Status: draft -->

<h1 style="visibility:hidden;">Boundary Jaccard (BJ Metric)</h1>

The recently introduced Boundary Jaccard [[1](#bj_iv)] metric is new evaluation metric for semantic segmentation algorithms. The BJ lays a focus on the segmentation accuracy along the contours. Describing this mathematically can be a bit awkward. Luckly, visualizing the regions of interest of the BJ metric can provide a more intuitive understaning of its caluclation. 

I'll quickly introduce the use case in which we will analyze the BJ metric. The Cityscapes dataset [[2](#cityscapes)] is a large-scale dataset consisting of urban driving scenes recorded across many German cities with high quality pixel-level annotations. Cityscapes is a commonly used dataset for the development of semantic image segmentation methods. We will use Fast-SCNN [[3](#fast_scnn)] as our semantic segmentation algorithm, since it produces fairly reasonable predictions on the Cityscapes dataset. 

### Introducing the BJ Metric

The authors of the BJ metric are inspired by the so-called BF [[4](#bf_bmvc)] score ("Boundary F1 score") and combining this with the common Jaccard index (a.k.a. Intersection over Union). All these metrics are calculated for each class $c$ of a segmentation map $S$. We denote the pixels of a segmentation map that belong to class $c$ as $S^{c}$. Here we also distinguish between the predicted segmentation map $S_{ps}$ and the ground truth segmentation map $S_{gt}$.

### References

<span id='bj_iv'>[1] Eduardo Fernandez-Moral, Renato Martins, Denis Wolf, Patrick Rives (IV 2018) [A new metric for evaluating semantic segmentation: leveraging global and contour accuracy](https://hal.inria.fr/hal-01581525/document)</span>

<span id='cityscapes'>[2] Marius Cordts, Mohamed Omran, Sebastian Ramos, Timo Rehfeld,
Markus Enzweiler, Rodrigo Benenson, Uwe Franke, Stefan Roth, Bernt Schiele (CVPR 2016) [The Cityscapes Dataset for Semantic Urban Scene Understanding](https://www.cityscapes-dataset.com/wordpress/wp-content/papercite-data/pdf/cordts2016cityscapes.pdf)</span>

<span id='fast_scnn'>[3] Rudra P. K. Poudel, Stephan Liwicki, Roberto Cipolla (BMVC 2019) [Fast-SCNN: Fast Semantic Segmentation Network](https://bmvc2019.org/wp-content/uploads/papers/0959-paper.pdf)- I use the [PyTorch implementation of Fast-SCNN](https://github.com/Tramac/Fast-SCNN-pytorch) by the GitHub User Tramac.</span>

<span id='bf_bmvc'>[4] Gabriela Csurka, Diane Larlus, Florent Perronnin (BMVC 2013) [What is a good evaluation measure for semantic segmentation?](http://www.bmva.org/bmvc/2013/Papers/paper0032/paper0032.pdf)</span>