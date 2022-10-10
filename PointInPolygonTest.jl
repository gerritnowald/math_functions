vert = [0 0;
		3 0;
		3 2;
		0 2;
		0 0]

point = [-1 1]


function isPointInside(vert,point)
	# A point is in a polygon, if a line from the point to infinity crosses the polygon an odd number of times.
	# Here, the line goes parallel to the x-axis in positive x-direction.
	# adapted from https://www.algorithms-and-technologies.com/point_in_polygon/python
	odd = false    
	for j in 1:size(vert)[1]-1          # for each edge check if the line crosses
		i = j + 1                       # next vertex
		if vert[j,2] != vert[i,2]       # edge not parallel to x-axis (singularity)
			# point between y-coordinates of edge
			if (vert[i,2] > point[2]) != (vert[j,2] > point[2])
				# x-coordinate of intersection
				Qx = (vert[j,1]-vert[i,1])*(point[2]-vert[i,2])/(vert[j,2]-vert[i,2]) + vert[i,1]
				if point[1] < Qx        # point left of edge
				    odd = ! odd         # line crosses edge
				end
			end
		end
	end
	return odd  # point is in polygon (not on the edge) if odd=true
end


isPointInside(vert,point)