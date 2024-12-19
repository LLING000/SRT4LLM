Expression_list=["regions","geometrical shapes"]
Expression=Expression_list[0] # choose the "expression" dimension

Shape_list=["rectangles","circles"]
Shape=Shape_list[0]

Prompt_list=["SP","GP","EP"]
Prompt=Prompt_list[0]

# rectangle-direction relation
rectangle_9=[]
rectangle_9.append("(2,14), (7,14), (7,17), (2,17), (2,14)")
rectangle_9.append("(9,14), (14,14), (14,18), (9,18), (9,14)")
rectangle_9.append("(19,14), (22,14), (22,18), (19,18), (19,14)")
rectangle_9.append("(3,8), (6,8), (6,11), (3,11), (3,8)")
rectangle_9.append("(10,7), (15,7), (15,11), (10,11), (10,7)")
rectangle_9.append("(19,6), (23,6), (23,11), (19,11), (19,6)")
rectangle_9.append("(2,0), (6,0), (6,5), (2,5), (2,0)")
rectangle_9.append("(10,1), (14,1), (14,4), (10,4), (10,1)")
rectangle_9.append("(18,1), (22,1), (22,5), (18,5), (18,1)")

direction_recs=[]
description_rec_x="rectangle x: "
description_rec_y="rectangle y: "
# Group 1
direction_recs.append(description_rec_x + rectangle_9[6] + "; " + description_rec_y + rectangle_9[0])
direction_recs.append(description_rec_x + rectangle_9[3] + "; " + description_rec_y + rectangle_9[6])
direction_recs.append(description_rec_x + rectangle_9[2] + "; " + description_rec_y + rectangle_9[0])
direction_recs.append(description_rec_x + rectangle_9[1] + "; " + description_rec_y + rectangle_9[2])
direction_recs.append(description_rec_x + rectangle_9[5] + "; " + description_rec_y + rectangle_9[1])
direction_recs.append(description_rec_x + rectangle_9[4] + "; " + description_rec_y + rectangle_9[6])
direction_recs.append(description_rec_x + rectangle_9[6] + "; " + description_rec_y + rectangle_9[5])
direction_recs.append(description_rec_x + rectangle_9[0] + "; " + description_rec_y + rectangle_9[5])
# Group 2
direction_recs.append(description_rec_x + rectangle_9[4] + "; " + description_rec_y + rectangle_9[1])
direction_recs.append(description_rec_x + rectangle_9[1] + "; " + description_rec_y + rectangle_9[7])
direction_recs.append(description_rec_x + rectangle_9[5] + "; " + description_rec_y + rectangle_9[4])
direction_recs.append(description_rec_x + rectangle_9[3] + "; " + description_rec_y + rectangle_9[4])
direction_recs.append(description_rec_x + rectangle_9[4] + "; " + description_rec_y + rectangle_9[0])
direction_recs.append(description_rec_x + rectangle_9[2] + "; " + description_rec_y + rectangle_9[3])
direction_recs.append(description_rec_x + rectangle_9[3] + "; " + description_rec_y + rectangle_9[1])
direction_recs.append(description_rec_x + rectangle_9[4] + "; " + description_rec_y + rectangle_9[8])
# Group 3
direction_recs.append(description_rec_x + rectangle_9[8] + "; " + description_rec_y + rectangle_9[5])
direction_recs.append(description_rec_x + rectangle_9[2] + "; " + description_rec_y + rectangle_9[5])
direction_recs.append(description_rec_x + rectangle_9[7] + "; " + description_rec_y + rectangle_9[6])
direction_recs.append(description_rec_x + rectangle_9[6] + "; " + description_rec_y + rectangle_9[8])
direction_recs.append(description_rec_x + rectangle_9[8] + "; " + description_rec_y + rectangle_9[3])
direction_recs.append(description_rec_x + rectangle_9[5] + "; " + description_rec_y + rectangle_9[7])
direction_recs.append(description_rec_x + rectangle_9[4] + "; " + description_rec_y + rectangle_9[2])
direction_recs.append(description_rec_x + rectangle_9[3] + "; " + description_rec_y + rectangle_9[7])

# circle-direction relation
circle_9=[]
circle_9.append("O:(4,16), r=2.5")
circle_9.append("O:(12,16), r=3")
circle_9.append("O:(21,16.5), r=3")
circle_9.append("O:(4.5,9), r=2.5")
circle_9.append("O:(13,9), r=3")
circle_9.append("O:(19.5,9.5), r=2.5")
circle_9.append("O:(3,3), r=3")
circle_9.append("O:(11,2.5), r=2.5")
circle_9.append("O:(20,3), r=3")

direction_cirs=[]
description_cir_x="circle x: "
description_cir_y="circle y: "
# Group 1
direction_cirs.append(description_cir_x + circle_9[6] + "; " + description_cir_y + circle_9[0])
direction_cirs.append(description_cir_x + circle_9[3] + "; " + description_cir_y + circle_9[6])
direction_cirs.append(description_cir_x + circle_9[2] + "; " + description_cir_y + circle_9[0])
direction_cirs.append(description_cir_x + circle_9[1] + "; " + description_cir_y + circle_9[2])
direction_cirs.append(description_cir_x + circle_9[5] + "; " + description_cir_y + circle_9[1])
direction_cirs.append(description_cir_x + circle_9[4] + "; " + description_cir_y + circle_9[6])
direction_cirs.append(description_cir_x + circle_9[6] + "; " + description_cir_y + circle_9[5])
direction_cirs.append(description_cir_x + circle_9[0] + "; " + description_cir_y + circle_9[5])
# Group 2
direction_cirs.append(description_cir_x + circle_9[4] + "; " + description_cir_y + circle_9[1])
direction_cirs.append(description_cir_x + circle_9[1] + "; " + description_cir_y + circle_9[7])
direction_cirs.append(description_cir_x + circle_9[5] + "; " + description_cir_y + circle_9[4])
direction_cirs.append(description_cir_x + circle_9[3] + "; " + description_cir_y + circle_9[4])
direction_cirs.append(description_cir_x + circle_9[4] + "; " + description_cir_y + circle_9[0])
direction_cirs.append(description_cir_x + circle_9[2] + "; " + description_cir_y + circle_9[3])
direction_cirs.append(description_cir_x + circle_9[3] + "; " + description_cir_y + circle_9[1])
direction_cirs.append(description_cir_x + circle_9[4] + "; " + description_cir_y + circle_9[8])
# Group 3
direction_cirs.append(description_cir_x + circle_9[8] + "; " + description_cir_y + circle_9[5])
direction_cirs.append(description_cir_x + circle_9[2] + "; " + description_cir_y + circle_9[5])
direction_cirs.append(description_cir_x + circle_9[7] + "; " + description_cir_y + circle_9[6])
direction_cirs.append(description_cir_x + circle_9[6] + "; " + description_cir_y + circle_9[8])
direction_cirs.append(description_cir_x + circle_9[8] + "; " + description_cir_y + circle_9[3])
direction_cirs.append(description_cir_x + circle_9[5] + "; " + description_cir_y + circle_9[7])
direction_cirs.append(description_cir_x + circle_9[4] + "; " + description_cir_y + circle_9[2])
direction_cirs.append(description_cir_x + circle_9[3] + "; " + description_cir_y + circle_9[7])

# The definition of direction relation
relation_dir=f""" 
    (1) Up(x,y): y is roughly above x. 
    (2) Down(x,y): y is roughly below x. 
    (3) Left(x,y): y is roughly to the left of x. 
    (4) Right(x,y): y is roughly to the right of x. 
    (5) Upper Left(x,y): y is roughly to the upper left of x. 
    (6) Lower Left(x,y): y is roughly to the lower left of x. 
    (7) Upper Right(x,y): y is roughly to the upper right of x. 
    (8) Lower Right(x,y): y is roughly to the lower right of x. 
"""

def get_completion(prompt):
    # Connect to your LLM to get the response.
    response="LLM Response"
    return response

if Prompt == "SP":
    if Shape == "rectangle":
        for i in range(24):
            direction_rec=direction_recs[i]
            prompt = f"""
            Your task is to determine the orientation relation between two closed {Expression} in the same coordinate system.
            Specifically, determine in what orientation y is in x.
            The eight kind of orientation relations will be delimited with ``` tag.
            ```{relation_dir}```.
            The two {Expression} are {Shape} that will be given their position by coordinates: {direction_rec}.
            """
            response = get_completion(prompt)
    elif Shape == "circle":
        for i in range(24):
            direction_cir=direction_cirs[i]
            prompt = f"""
            Your task is to determine the orientation relation between two closed {Expression} in the same coordinate system.
            Specifically, determine in what orientation y is in x.
            The eight kind of orientation relations will be delimited with ``` tag.
            ```{relation_dir}```.
            The two {Expression} are {Shape} that will be given their position by the center O and the radius r: {direction_cir}.
            """
            response = get_completion(prompt)
elif Prompt == "GP":
    if Shape == "rectangle":
        for i in range(24):
            direction_rec=direction_recs[i]
            prompt = f"""
            Your task is to determine the orientation relation between two closed {Expression} in the same coordinate system.
            Specifically, determine in what orientation y is in x.
            The eight kind of orientation relations will be delimited with ``` tag.
            ```{relation_dir}```.
            The two {Expression} are {Shape} that will be given their position by coordinates: {direction_rec}.
            Pay attention to the following points in responding:
            (1) - Compare the range of x and y coordinates occupied by the two {Expression}, don't just focus on one side of the coordinate.
            (2) - If most of the x or y coordinate ranges of two {Expression} overlap, the ranges can be roughly considered to coincide in that coordinate. 
            """
            response = get_completion(prompt)
    elif Shape == "circle":
        for i in range(24):
            direction_cir=direction_cirs[i]
            prompt = f"""
            Your task is to determine the orientation relation between two closed {Expression} in the same coordinate system.
            Specifically, determine in what orientation y is in x.
            The eight kind of orientation relations will be delimited with ``` tag.
            ```{relation_dir}```.
            The two {Expression} are {Shape} that will be given their position by the center O and the radius r: {direction_cir}.
            Pay attention to the following points in responding:
            (1) - Based on the center coordinates and radius, compare the range of x and y coordinates occupied by the two {Expression} and don't just focus on one side of the coordinate.
            (2) - If most of the x or y coordinate ranges of two {Expression} overlap, the ranges can be roughly considered to coincide in that coordinate. 
            """
            response = get_completion(prompt)
elif Prompt == "EP":
    if Shape == "rectangle":
        for i in range(24):
            direction_rec=direction_recs[i]
            prompt = f"""
            Your task is to determine the orientation relation between two closed {Expression} in the same coordinate system.
            Specifically, determine in what orientation y is in x.
            The eight kind of orientation relations will be delimited with ``` tag.
            ```{relation_dir}```.
            You will be given two cases to learn how to reason the quesion out. 
            Case 1 - The two {Expression} are {Shape} that will be given their position by coordinates: rectangle x: (5,11), (10,11), (10,15), (5,15), (5,11); rectangle y: (4,1), (9,1), (9,7), (4,7), (4,1).
            Answer 1 - Based on the given coordinate information, the position of the two rectangles in the coordinate system can be determined: 
            rectangle x: x-coordinate ranges from 5 to 10, y-coordinate ranges from 11 to 15.
            rectangle y: x coordinate ranges from 4 to 9, y coordinate ranges from 1 to 7.
            Next, reason about the orientation relation between two rectangles:
            (1) The x-coordinate ranges of the two rectangles overlap so much that it can be roughly assumed that the two have the same range in x-coordinate.
            (2) The y-coordinate ranges of the two rectangles do not overlap at all, and the y-coordinate of rectangle y is smaller than rectangle x. It can be assumed that y is below x.
            Therefore, it is concluded that the two rectangles are Down(x,y).

            Case 2 - The two {Expression} are {Shape} that will be given their position by coordinates: rectangle x: (11,0), (16,0), (16,5), (11,5), (11,0); rectangle y: (17,7), (21,7), (21,12), (17,12), (17,7).
            Answer 2 - Based on the given coordinate information, the position of the two rectangles in the coordinate system can be determined: 
            rectangle x: x-coordinate ranges from 11 to 16, y-coordinate ranges from 0 to 5.
            rectangle y: x coordinate ranges from 17 to 21, y coordinate ranges from 7 to 12.
            Next, reason about the orientation relation between two rectangles:
            (1) The x-coordinate ranges of the two rectangles do not overlap at all, and the x-coordinate of rectangle y is greater than rectangle x. It can be assumed that y is to the right of x.
            (2) The y-coordinate ranges of the two rectangles do not overlap at all, and the y-coordinate of rectangle y is greater than rectangle x. It can be assumed that y is above x.
            Therefore, it is concluded that the two rectangles are Upper Right(x,y).

            Question - The two {Expression} are {Shape} that will be given their position by coordinates: {direction_rec}.
            """
            response = get_completion(prompt)
    elif Shape == "circle":
        for i in range(24):
            direction_cir=direction_cirs[i]
            prompt = f"""
            Your task is to determine the orientation relation between two closed {Expression} in the same coordinate system.
            Specifically, determine in what orientation y is in x.
            The eight kind of orientation relations will be delimited with ``` tag.
            ```{relation_dir}```.
            You will be given two cases to learn how to reason the quesion out. 
            Case 1 - The two {Expression} are {Shape} that will be given their position by the center O and the radius r: circle x: O:(7,3.5), r=2.5; rectangle y: O:(8,12), r=2.5.
            Answer 1 - Based on the given coordinate information, the position of the two circles in the coordinate system can be determined: 
            circle x: x-coordinate ranges from 4.5 to 9.5, y-coordinate ranges from 1 to 6.
            circle y: x coordinate ranges from 5.5 to 10.5, y coordinate ranges from 9.5 to 14.5.
            Next, reason about the orientation relation between two circles:
            (1) The x-coordinate ranges of the two circles overlap so much that it can be roughly assumed that the two have the same range in x-coordinate.
            (2) The y-coordinate ranges of the two circles do not overlap at all, and the y-coordinate of circle y is greater than circle x. It can be assumed that y is above x.
            Therefore, it is concluded that the two circles are Up(x,y).

            Case 2 - The two {Expression} are {Shape} that will be given their position by the center O and the radius r: circle x: O:(19,11), r=3; rectangle y: O:(14,4.5), r=2.5.
            Answer 2 - Based on the given coordinate information, the position of the two circles in the coordinate system can be determined: 
            circle x: x-coordinate ranges from 16 to 22, y-coordinate ranges from 8 to 14.
            circle y: x coordinate ranges from 11.5 to 16.5, y coordinate ranges from 2 to 7.
            Next, reason about the orientation relation between two circles:
            (1) The x-coordinate ranges of the two circles overlap so little that they can be considered not to overlap. The x-coordinate of rectangle y is smaller than rectangle x. It can be assumed that y is to the left of x.
            (2) The y-coordinate ranges of the two rectangles do not overlap at all, and the y-coordinate of rectangle y is smaller than rectangle x. It can be assumed that y is below x.
            Therefore, it is concluded that the two rectangles are Lower Left(x,y).

            Question - The two {Expression} are {Shape} that will be given their position by the center O and the radius r: {direction_cir}.
            """
            response = get_completion(prompt)