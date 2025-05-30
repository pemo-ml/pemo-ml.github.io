Title: Tree Diagram for Outdoor Datasets
Date: 2021-07-27 23:00
Category: Visualization
Tags: d3.js, datasets
Slug: outdoor-datasets-tree-diagram
Authors: Peter Mortimer
Summary: An interactive tree diagram for reviewing the semantic classes of different Outdoor datasets.
Status: draft

Many new datasets for the semantic segmentation of driving scenes have been released in recent years. It is not always clear how many of the semantic classes of the datasets overlap and how fine-granular the annotation of each dataset is.

This interactive tree diagram allows you to unfold the common categories of these driving datasets and to observe which of the given datasets can be used for training on this level of granularity.

<div id="tree-div" style="text-align: center"></div>

This is the text after the tree diagram.

<link rel="stylesheet" href="extra/vis/tree-diagram/style.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.17/d3.min.js"></script>
<script src="extra/vis/tree-diagram/tree.js"></script>

