Title: Visual Analysis of the Earth Mover's Distance
Date: 2019-05-14 10:30
Category: Python
Tags: Earth Mover's Distance, Point Clouds, 3D Machine Learning
Slug: earth-movers-distance
Authors: Peter Mortimer
Summary: What exactly is the Earth Mover's distance and how is it used in 3D Machine Learning?
Status: draft

Many recent research papers [[1](#pcn),[2](#pointoutnet)] focused on neural networks for 3D point cloud data use one of the two distance metrics as loss function or evaluation metric: the Chamfer distance ($D_{CD}$) and the Earth Mover's distance ($D_{EMD}$). The calculation of the Chamfer distance is easy to grasp, while the Earth Mover's distance is less clearly defined. In this post I want to give an overview of the Earth Mover's distance and in particular how it is used for training point cloud data. The Earth Mover's distance is also known under the term 1-Wasserstein metric, but we will refer to it as the Earth Mover's distance in this post.

## Introduction

Let's first look at the mathematical definition of the Earth Mover's distance:

$$ D_{EMD}(S_{1},S_{2}) = \min_{\phi: S_{1} \to S_{2} } \frac{1}{|S_{1}|} \sum_{x \in S_{1}} \| x - \phi(x) \|_{2}$$

The function $\phi$ is a bijection (this also implies that $D_{EMD}$ is only defined for $|S_{1}| = |S_{2}|$). This can be seen as a matching between points in $S_{1}$ to points in $S_{2}$. The matching with the minimal euclidean distance therefore describes the Earth Mover's distance.
A common interpretation of the Earth Mover's distance describes the measure as the minimum amount of work needed to spread a mass of earth collected in piles to fill a set of holes in the same given space [[4](#cvonline_emd),[5](#translocation)]. In this interpretation work is determined both by the weight of the earth moved and the distance that the earth had to be moved to fill the holes.


## References

<span id='pcn'>[1] Yuan, Khot, Held, Mertz, Herbert (3DV 2018) [PCN: Point Completion Network](https://www.cs.cmu.edu/~wyuan1/pcn/)</span>

<span id='pointoutnet'>[2] Fan, Su, Leonidas (CVPR 2017) [A Point Set Generation Network for 3D Object Reconstruction from a Single Image](https://arxiv.org/abs/1612.00603)</span>

<span id='swd'>[3] Lee, Batra, Baig, Ulbricht (CVPR 2019) [Sliced Wasserstein Discrepancy for Unsupervised Domain Adaptation.](https://arxiv.org/abs/1903.04064)</span>

<span id='cvonline_emd'>[4] CVOnline on the Earth Mover's Distance [The Earth Mover's Distance](http://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/RUBNER/emd.htm)</span>


<span id='translocation'>[5] Kantorovitch, Lee (Management Science 1958) [On the Translocation of Masses](https://web.eecs.umich.edu/~pettie/matching/Kantorovitch-translocation-of-masses-1942.pdf)</span>

