Title: Overview of the Earth Mover's Distance
Date: 2019-05-14 10:30
Category: Python
Tags: Earth Mover's Distance, Point Clouds, 3D Machine Learning
Slug: earth-movers-distance
Authors: Peter Mortimer
Summary: What exactly is the Earth Mover's distance and how is it used in 3D Machine Learning?
Status: draft

Many recent research papers [[1](#pcn),[2](#pointoutnet)] focused on neural networks for point cloud data use one of the two distance metrics as loss function or evaluation metric: the Chamfer distance ($D_{CD}$) and the Earth Mover's distance ($D_{EMD}$). The calculation of the Chamfer distance is easy to grasp, while the Earth Mover's distance is less clearly defined. In this post I want to give a quick overview of the Earth Mover's distance and in particular how it is used for training point cloud data. The Earth Mover's distance is also known under the term Wasserstein metric, but we will refer to it as the Earth Mover's distance in this post.

## References

<span id='pcn'>[1] Yuan, Khot, Held, Mertz, Herbert (3DV 2018) [PCN: Point Completion Network](https://www.cs.cmu.edu/~wyuan1/pcn/)</span>

<span id='pointoutnet'>[2] Fan, Su, Leonidas (CVPR 2017) [A Point Set Generation Network for 3D Object Reconstruction from a Single Image](https://arxiv.org/abs/1612.00603)</span>
