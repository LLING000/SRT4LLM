Expression_list=["regions","geometrical shapes"]
Expression=Expression_list[0] # choose the "expression" dimension

Shape_list=["rectangles","circles"]
Shape=Shape_list[0]

Prompt_list=["SP","GP","EP"]
Prompt=Prompt_list[0]

# rectangle-topological relation
topological_recs=[]
# horizontal layout
# DC
topological_recs.append("rectangle x: (1,1), (3,1), (3,4), (1,4), (1,1); rectangle y: (4,2), (6,2), (6,3), (4,3), (4,2)")
# EC
topological_recs.append("rectangle x: (1,6), (3,6), (3,9), (1,9), (1,6); rectangle y: (3,7), (5,7), (5,8), (3,8), (3,7)")
# PO
topological_recs.append("rectangle x: (1,4), (3,4), (3,7), (1,7), (1,4); rectangle y: (2,5), (4,5), (4,6), (2,6), (2,5)")
# TPP
topological_recs.append("rectangle x: (9,2), (11,2), (11,3), (9,3), (9,2); rectangle y: (7,1), (11,1), (11,4), (7,4), (7,1)")
# NTPP
topological_recs.append("rectangle x: (9,4), (11,4), (11,5), (9,5), (9,4); rectangle y: (5,3), (12,3), (12,6), (5,6), (5,3)")
# TPPi
topological_recs.append("rectangle x: (6,7), (10,7), (10,10), (6,10), (6,7); rectangle y: (8,8), (10,8), (10,9), (8,9), (8,8)")
# NTPPi
topological_recs.append("rectangle x: (10,4), (17,4), (17,7), (10,7), (10,4); rectangle y: (11,5), (13,5), (13,6), (11,6), (11,5)")
# EQ
topological_recs.append("rectangle x: (6,5), (3,5), (3,3), (6,3), (6,5); rectangle y: (3,3), (6,3), (6,5), (3,5), (3,3)")

# vertical layout
# DC
topological_recs.append("rectangle x: (1,1), (4,1), (4,3), (1,3), (1,1); rectangle y: (2,4), (3,4), (3,6), (2,6), (2,4)")
# EC
topological_recs.append("rectangle x: (6,1), (7,1), (7,3), (6,3), (6,1); rectangle y: (5,3), (8,3), (8,5), (5,5), (5,3)")
# PO
topological_recs.append("rectangle x: (4,6), (7,6), (7,8), (4,8), (4,6); rectangle y: (5,7), (6,7), (6,9), (5,9), (5,7)")
# TPP
topological_recs.append("rectangle x: (3,11), (6,11), (6,12), (3,12), (3,11); rectangle y: (2,9), (7,9), (7,12), (2,12), (2,9)")
# NTPP
topological_recs.append("rectangle x: (10,10), (11,10), (11,12), (10,12), (10,10); rectangle y: (9,7), (12,7), (12,13), (9,13), (9,7)")
# TPPi
topological_recs.append("rectangle x: (8,5), (13,5), (13,8), (8,8), (8,5); rectangle y: (10,5), (12,5), (12,6), (10,6), (10,5)")
# NTPPi
topological_recs.append("rectangle x: (11,1), (15,1), (15,7), (11,7), (11,1); rectangle y: (12,4), (14,4), (14,6), (12,6), (12,4)")
# EQ
topological_recs.append("rectangle x: (3,8), (0,8), (0,6), (3,6), (3,8); rectangle y: (0,6), (3,6), (3,8), (0,8), (0,6)")

# diagonal layout
# DC
topological_recs.append("rectangle x: (1,8), (3,8), (3,11), (1,11), (1,8); rectangle y: (4,5), (7,5), (7,7), (4,7), (4,5)")
# EC
topological_recs.append("rectangle x: (3,5), (5,5), (5,8), (3,8), (3,5); rectangle y: (4,8), (7,8), (7,10), (4,10), (4,8)")
# PO
topological_recs.append("rectangle x: (1,3), (5,3), (5,6), (1,6), (1,3); rectangle y: (3,1), (6,1), (6,5), (3,5), (3,1)")
# TPP
topological_recs.append("rectangle x: (6,2), (8,2), (8,3), (6,3), (6,2); rectangle y: (7,1), (11,1), (11,4), (7,4), (7,1)")
# NTPP
topological_recs.append("rectangle x: (9,7), (10,7), (10,9), (9,9), (9,7); rectangle y: (8,6), (14,6), (14,12), (8,12), (8,6)")
# TPPi
topological_recs.append("rectangle x: (11,4), (15,4), (15,9), (11,9), (11,4); rectangle y: (11,4), (12,4), (12,7), (11,7), (11,4)")
# NTPPi
topological_recs.append("rectangle x: (9,1), (16,1), (16,5), (9,5), (9,1); rectangle y: (10,3), (12,3), (12,4), (10,4), (10,3)")
# EQ
topological_recs.append("rectangle x: (3,4), (0,4), (0,2), (3,2), (3,4); rectangle y: (0,2), (3,2), (3,4), (0,4), (0,2)")


# circle-topological relation
topological_cirs=[]
# 左右
# DC
topological_cirs.append("circle x: O:(3,2), r=2; circle y: O:(9,2), r=2")
# EC
topological_cirs.append("circle x: O:(3,5), r=2; circle y: O:(7,5), r=2")
# PO
topological_cirs.append("circle x: O:(4,9), r=2; circle y: O:(7,9), r=2")
# TPP
topological_cirs.append("circle x: O:(13,4), r=1; circle y: O:(12,4), r=2")
# NTPP
topological_cirs.append("circle x: O:(12,10), r=1; circle y: O:(13,10), r=3")
# TPPi
topological_cirs.append("circle x: O:(10,8), r=2; circle y: O:(9,8), r=1")
# NTPPi
topological_cirs.append("circle x: O:(16,4), r=3; circle y: O:(17,4), r=1")
# EQ
topological_cirs.append("circle x: O:(6,3), r=2; circle y: r=2, O:(6,3)")

# 上下
# DC
topological_cirs.append("circle x: O:(3,3), r=2; circle y: O:(3,8), r=2")
# EC
topological_cirs.append("circle x: O:(6,2), r=2; circle y: O:(6,6), r=2")
# PO
topological_cirs.append("circle x: O:(9,3), r=2; circle y: O:(9,6), r=2")
# TPP
topological_cirs.append("circle x: O:(5,11), r=1; circle y: O:(5,10), r=2")
# NTPP
topological_cirs.append("circle x: O:(11,10), r=1; circle y: O:(11,9), r=3")
# TPPi
topological_cirs.append("circle x: O:(16,8), r=2; circle y: O:(16,9), r=1")
# NTPPi
topological_cirs.append("circle x: O:(14,3), r=3; circle y: O:(14,2), r=1")
# EQ
topological_cirs.append("circle x: O:(17,4), r=2; circle y: r=2, O:(17,4)")

# 斜向
# DC
topological_cirs.append("circle x: O:(3,2), r=2; circle y: O:(6,6), r=2")
# EC
topological_cirs.append("circle x: O:(4,6), r=2; circle y: O:(7,2), r=3")
# PO
topological_cirs.append("circle x: O:(2,8), r=2; circle y: O:(4,10), r=2")
# TPP
topological_cirs.append("circle x: O:(11,0), r=2; circle y: O:(14,4), r=7")
# NTPP
topological_cirs.append("circle x: O:(17,4), r=1; circle y: O:(16,3), r=3")
# TPPi
topological_cirs.append("circle x: O:(12,7), r=7; circle y: O:(8,10), r=2")
# NTPPi
topological_cirs.append("circle x: O:(14,9), r=3; circle y: O:(13,8), r=1")
# EQ
topological_cirs.append("circle x: O:(11,5), r=2; circle y: r=2, O:(11,5)")


# The definition of topological relation
relation_topo=f""" 
    (1) DC(x,y): x is disconnected from y. 
    (2) EC(x,y): x is externally connected to y without any overlap. 
    (3) PO(x,y): x partially overlaps y, with neither being a part of the other. 
    (4) TPP(x,y): x is a tangential proper part of y. 
    (5) NTPP(x,y): x is a nontangential proper part of y. 
    (6) TPPi(x,y): y is a tangential proper part of x. 
    (7) NTPPi(x,y): y is a nontangential proper part of x. 
    (8) EQ(x,y): x is identical with y. 
"""

def get_completion(prompt):
    # Connect to your LLM to get the response.
    response="LLM Response"
    return response

if Prompt == "SP": # 调用llm得到回答: 无思维链
    if Shape == "rectangle":
        for i in range(24):
            topological_rec=topological_recs[i]
            prompt = f"""
            Your task is to determine the topological relation between two closed {Expression} in the same coordinate system.
            The eight kind of topological relations will be delimited with ``` tag.
            ```{relation_topo}```.
            The two {Expression} are {Shape} that will be given their position by coordinates: {topological_rec}.
            """
            response = get_completion(prompt)
    elif Shape == "circle":
        for i in range(24):
            topological_cir=topological_cirs[i]
            prompt = f"""
            Your task is to determine the topological relation between two closed {Expression} in the same coordinate system.
            The eight kind of topological relations will be delimited with ``` tag.
            ```{relation_topo}```.
            The two {Expression} are {Shape} that will be given their position by the center O and the radius r: {topological_cir}.
            """
            response = get_completion(prompt)
elif Prompt == "GP":
    if Shape == "rectangle":
        for i in range(24):
            topological_rec=topological_recs[i]
            prompt = f"""
            Your task is to determine the topological relation between two closed {Expression} in the same coordinate system.
            The eight kind of topological relations will be delimited with ``` tag.
            ```{relation_topo}```.
            The two {Expression} are {Shape} that will be given their position by coordinates: {topological_rec}.
            Pay attention to the following points in responding:
            (1) - By specifying the range of x-coordinate and y-coordinate, clearly define the positions of two {Expression} in the coordinate system.
            (2) - Two rectangles can only be overlapping if their x-coordinate and y-coordinate overlap at the same time.
            (3) - TPP, NTPP, TPPi, NTPPi and EQ are special cases of PO and should be categorized separately if their definitions are met. If not, categorized as PO.
            """
            response = get_completion(prompt)
    elif Shape == "circle":
        for i in range(24):
            topological_cir=topological_cirs[i]
            prompt = f"""
            Your task is to determine the topological relation between two closed {Expression} in the same coordinate system.
            The eight kind of topological relations will be delimited with ``` tag.
            ```{relation_topo}```.
            The two {Expression} are {Shape} that will be given their position by the center O and the radius r: {topological_cir}.
            Pay attention to the following points in responding:
            (1) - This method may be effective: 
            calculate the distance between the centers of two circles and compare it separately with the sum and the absolute difference of their radii.
            If distance > sum: it is DC(x,y).
            If distance = sum: it is EC(x,y).
            If difference < distance < sum: it is PO(x,y).
            If distance = difference: it is TPP(x,y) or TPPi(x,y).
            If distance < difference: it is NTPP(x,y) or NTPPi(x,y).
            If the centers and radii are same: it is EQ(x,y).
            (2) - TPP, NTPP, TPPi, NTPPi and EQ are special cases of PO and should be categorized separately if their definitions are met. If not, categorized as PO.
            """
            response = get_completion(prompt)
elif Prompt == "EP":
    if Shape == "rectangle":
        for i in range(24):
            topological_rec=topological_recs[i]
            prompt = f"""
            Your task is to determine the topological relation between two closed {Expression} in the same coordinate system.
            The eight kind of topological relations will be delimited with ``` tag.
            ```{relation_topo}```.
            You will be given two cases to learn how to reason the quesion out. 
            Case 1 - The two {Expression} are {Shape} that will be given their position by coordinates: rectangle x: (5,6), (7,6), (7,7), (5,7), (5,6); rectangle y: (4,5), (8,5), (8,8), (4,8), (4,5).
            Answer 1 - Based on the given coordinate information, the position of the two circles in the coordinate system can be determined: 
            rectangle x: x-coordinate ranges from 5 to 7, y-coordinate ranges from 6 to 7.
            rectangle y: x coordinate ranges from 4 to 8, y coordinate ranges from 5 to 8.
            Next, reason about the topological relation between two rectangles:
            1. The two rectangles overlap in both the x and y coordinate ranges, so it is not DC(x,y) or EC(x,y).
            2. Rectangle x's x and y coordinates are both completely contained in rectangle y, so they are not partially overlapping or identical. It is a TPP(x,y) or NTPP(x,y) relation.
            3. Rectangle x and rectangle y are not tangent, so it is a NTPP(x,y) relationship.
            Therefore, it is concluded that the two rectangles are NTPP(x,y).

            Case 2 - The two {Expression} are {Shape} that will be given their position by coordinates: rectangle x: (1,2), (3,2), (3,5), (1,5), (1,2); rectangle y: (3,3), (5,3), (5,4), (3,4), (3,3).
            Answer 2 - Based on the given coordinate information, the position of the two rectangles in the coordinate system can be determined: 
            rectangle x: x-coordinate ranges from 1 to 3, y-coordinate ranges from 2 to 5.
            rectangle y: x coordinate ranges from 3 to 5, y coordinate ranges from 3 to 4.
            Next, reason about the topological relation between two rectangles:
            1. The y-coordinate ranges of the two rectangles overlap, but the x-coordinate ranges do not, so it is DC(x,y) or EC(x,y), not the others.
            2. The x-coordinate ranges of the two rectangles do not overlap, but are connected, indicating that the two rectangles are externally connected, so it is EC(x,y).
            Therefore, it is concluded that the two rectangles are EC(x,y).

            Qustion - The two {Expression} are {Shape} that will be given their position by coordinates: {topological_rec}.
            """
            response = get_completion(prompt)
    elif Shape == "circle":
        for i in range(24):
            topological_cir=topological_cirs[i]
            prompt = f"""
            Your task is to determine the topological relation between two closed {Expression} in the same coordinate system.
            The eight kind of topological relations will be delimited with ``` tag.
            ```{relation_topo}```.
            You will be given two cases to learn how to reason the quesion out. 
            Case 1 - The two {Expression} are {Shape} that will be given their position by the center O and the radius r: circle x: O:(8,3), r=1; circle y: O:(7,3), r=2.
            Answer 1 - Based on the given coordinate information, the position of the two circles in the coordinate system can be determined: 
            circle x: the center is (8,3), the radii is 1.
            circle y: the center is (7,3), the radii is 2.
            Next, calculate the distance between the centers of two circles and compare it separately with the sum and the absolute difference of their radii.
            (1) The distance between the centers of the two circles: distance = sqrt((7-8)^2+(3-3)^2) = sqrt(1) = 1.
            (2) The sum of the radii of two circles: sum = 2+1 = 3.
            (3) The difference between the radii of the two circles: difference = |2-1| = 1.
            Since distance = difference, so the two circles are internally tangent and it is TPP(x,y) or TPPi(x,y).
            And because circle x is smaller than circle y, so x is a tangential proper part of y.
            Therefore, the relation between the two circles is TPP(x,y).

            Case 2 - The two {Expression} are {Shape} that will be given their position by the center O and the radius r: circle x: O:(10,8), r=3; circle y: O:(11,8), r=1.
            Answer 2 - Based on the given coordinate information, the position of the two circles in the coordinate system can be determined: 
            circle x: the center is (10,8), the radii is 3.
            circle y: the center is (11,8), the radii is 1.
            Next, calculate the distance between the centers of two circles and compare it separately with the sum and the absolute difference of their radii.
            (1) The distance between the centers of the two circles: distance = sqrt((11-10)^2+(8-8)^2) = sqrt(1) = 1.
            (2) The sum of the radii of two circles: sum = 1+3 = 4.
            (3) The difference between the radii of the two circles: difference = |1-3| = 2.
            Since distance < difference, so the relation of two circles is NTPP(x,y) or NTPPi(x,y).
            And because circle y is smaller than circle x, so y is a nontangential proper part of x.
            Therefore, the relation between the two circles is NTPPi(x,y).

            Qustion - The two {Expression} are {Shape} that will be given their position by the center O and the radius r: {topological_cir}.
            """
            response = get_completion(prompt)