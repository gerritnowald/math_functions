using Plots

# ----------------------------------------------------------------------
# inputs

Vertices = [
    0 0;
    1.75 4;
    1.5 6;
    1 7;
    0.25 6;
    0 5;
    -0.25 6;
    -1 7;
    -1.5 6;
    -1.75 4;
    0 0
    ]

N = 10000

# ----------------------------------------------------------------------
# functions

function isPointInside(vert,point)
	# A point is in a polygon, if a line from the point to infinity crosses the polygon an odd number of times.
	# Here, the line goes parallel to the x-axis in positive x-direction.
	# adapted from https://www.algorithms-and-technologies.com/point_in_polygon/python
	odd = false
	for j in 1:size(vert)[1]-1      # for each edge check if the line crosses
		i = j + 1                   # next vertex
        # edge parallel to x-axis (singularity)
		if vert[j,2] == vert[i,2]
            continue
        end
        # point not between y-coordinates of edge
        if (vert[i,2] > point[2]) == (vert[j,2] > point[2])
            continue
        end
        # x-coordinate of intersection
        Qx = (vert[j,1]-vert[i,1])*(point[2]-vert[i,2])/(vert[j,2]-vert[i,2]) + vert[i,1]
        if point[1] < Qx    # point left of edge
            odd = ! odd     # line crosses edge
        end
	end
	return odd  # point is in polygon (not on the edge) if odd=true
end

# ----------------------------------------------------------------------
# plot

points = [rand(N,1).*6 .- 3   rand(N,1).*10 .- 2]

p = plot()

start = time()
for i=1:size(points)[1]
    point = points[i,:]
    if isPointInside(Vertices,point)
        style = "yellow"
    else
        style = "blue"
    end
    scatter!(p, [point[1]],[point[2]], label="", color = style)
end
println(time() - start)

display(p)
