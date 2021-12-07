# Data visulaization

sum(is.na(wine))

# Identification of near zero variance predictors
nearZeroVar(train_set[, xcol], saveMetrics = TRUE)


# Compactly Display the Structure of an Arbitrary R Object
str(train_set)

# Statistics summary
summary(train_set)

# Install and load the libraries used for visualization
# The 'load_lib' function was defined earlier. 
load_lib(c("gridExtra", "ggridges", "ggplot2","gtable", "grid", "egg"))
grid_arrange_shared_legend <-
function(...,ncol = length(list(...)), nrow = 1,position = c("bottom", "right")) {

plots <- list(...)
position <- match.arg(position)
g <-ggplotGrob(plots[[1]] + theme(legend.position = position))$grobs 
legend <- g[[which(sapply(g, function(x)x$name) == "guide-box")]] 
lheight <- sum(legend$height) 
lwidth <- sum(legend$width) 
gl <- lapply(plots, function(x)x + theme(legend.position = "none"))
gl <- c(gl, ncol = ncol, nrow = nrow)
combined <- switch( position,
"bottom" = arrangeGrob( do.call(arrangeGrob, gl), legend,
ncol = 1,heights = unit.c(unit(1, "npc") - lheight, lheight)),
"right" = arrangeGrob(do.call(arrangeGrob, gl),legend,ncol = 2,
 widths = unit.c(unit(1, "npc") - lwidth, lwidth) ) )
 grid.newpage()
 grid.draw(combined)
 
 # return gtable invisibly
 invisible(combined)
 }
