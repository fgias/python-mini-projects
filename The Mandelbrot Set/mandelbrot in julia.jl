using Plots

pointsx = []
pointsy = []

step=0.008

for i = -2:step:2
    print(i, "\n")
    for j = -2:step:2
        c = i + j*1im
        z = 0
        diverge = false
        for n = 1:20
            z = z^2 + c
            if abs(z) > 2
                diverge = true
                break
            end
        end

        if diverge == false
            append!(pointsx, i)
            append!(pointsy, j)
        end
    end
end

plot(pointsx, pointsy, 
seriestype = :scatter, markersize=.5,
legend=false)