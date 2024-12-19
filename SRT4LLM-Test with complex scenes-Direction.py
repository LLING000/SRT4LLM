Expression_list=["regions","geometrical shapes"]
Expression=Expression_list[1] # choose the "expression" dimension

Prompt_list=["SP","GP","EP"]
Prompt=Prompt_list[0] # choose the prompt template

polygon=[]
polygon.append("(0,0)")
# Point 1-7
polygon.append("(17,9)")
polygon.append("(22,10)")
polygon.append("(24,8)")
polygon.append("(25,3)")
polygon.append("(28,8)")
polygon.append("(61,4)")
polygon.append("(63,8)")
# Line 8-12
polygon.append("(19,9), (21,7), (24,6), (28,6)")
polygon.append("(36,6), (38,5), (41,2)")
polygon.append("(39,15), (41,15), (42,14)")
polygon.append("(47,1), (48,4), (48,6)")
polygon.append("(61,9), (65,7), (66,8)")
# Polygon 13-18
polygon.append("(3,26), (6,24), (10,24), (11,26), (9,31), (6,32), (4,30), (3,26)")
polygon.append("(6,23), (12,23), (14,26), (8,29), (6,23)")
polygon.append("(5,40), (8,38), (10,40), (9,48), (6,46), (4,43), (5,40)")
polygon.append("(11,41), (12,39), (15,41), (14,46), (11,47), (10,45), (11,41)")
polygon.append("(17,37), (18,38), (24,36), (31,35), (30,32), (27,31), (22,30), (19,33), (17,37)")
polygon.append("(25,36), (28,37), (31,37), (35,36), (36,34), (32,33), (28,33), (25,36)")
# Polygon 19-24
polygon.append("(19,26), (20,24), (22,23), (25,25), (26,27), (22,28), (19,26)")
polygon.append("(18,26), (19,23), (22,21), (26,20), (28,23), (27,26), (26,27), (21,28), (18,26)")
polygon.append("(18,15), (20,12), (26,11), (28,12), (27,13), (25,13), (25,15), (27,15), (28,16), (27,18), (25,19), (24,17), (22,17), (22,18), (20,19), (19,18), (18,15)")
polygon.append("(16,6), (16,5), (19,4), (25,4), (24,5), (18,6), (17,7), (16,6)")
polygon.append("(34,27), (32,24), (33,23), (34,23), (35,24), (34,27)")
polygon.append("(30,26), (31,21), (37,20), (38,23), (36,29), (33,28), (30,26)")
# Polygon 25-30
polygon.append("(36,14), (41,12), (45,12), (45,14), (43,16), (40,17), (37,16), (36,14)")
polygon.append("(35,4), (36,2), (38,2), (39,3), (37,5), (36,5), (35,4)")
polygon.append("(38,37), (39,35), (43,34), (50,34), (52,37), (50,37), (49,35), (43,36), (41,37), (39,39), (38,37)")
polygon.append("(40,40), (43,37), (48,36), (49,38), (48,39), (49,40), (48,41), (41,43), (40,40)")
polygon.append("(45,21), (47,20), (48,22), (46,22), (45,21)")
polygon.append("(44,21), (45,20), (48,19), (50,20), (49,23), (46,24), (45,23), (44,21)")
# Polygon 31-36
polygon.append("(44,3), (45,2), (48,1), (49,3), (47,5), (45,4), (44,3)")
polygon.append("(52,24), (53,22), (54,21), (56,22), (56,25), (53,25), (52,24)")
polygon.append("(57,22), (58,21), (61,21), (62,23), (61,25), (57,25), (57,22)")
polygon.append("(50,17), (50,16), (52,14), (54,14), (56,16), (56,18), (52,19), (50,17)")
polygon.append("(54,17), (54,15), (58,13), (60,14), (61,15), (58,18), (56,18), (54,17)")
polygon.append("(57,3), (61,1), (62,2), (60,4), (58,4), (57,3)")

direction_test=[]
description_g1="polygon x: "
description_g2="polygon y: "
description_p1="point x: "
description_p2="point y: "
description_l1="line x: "
description_l2="line y: "

# Direction test scenes
direction_test.append(description_g1 + polygon[16] + "; " + description_g2 + polygon[15])
direction_test.append(description_g1 + polygon[17] + "; " + description_g2 + polygon[18])
direction_test.append(description_g1 + polygon[28] + "; " + description_g2 + polygon[27])
direction_test.append(description_g1 + polygon[20] + "; " + description_g2 + polygon[19])
direction_test.append(description_g1 + polygon[34] + "; " + description_g2 + polygon[14])
direction_test.append(description_g1 + polygon[22] + "; " + description_p2 + polygon[2])
direction_test.append(description_p1 + polygon[4] + "; " + description_p2 + polygon[8])
direction_test.append(description_l1 + polygon[10] + "; " + description_g2 + polygon[25])
direction_test.append(description_l1 + polygon[11] + "; " + description_l2 + polygon[12])
direction_test.append(description_p1 + polygon[9] + "; " + description_g2 + polygon[26])

direction_test.append(description_g1 + polygon[22] + "; " + description_g2 + polygon[16])
direction_test.append(description_g1 + polygon[36] + "; " + description_g2 + polygon[15])
direction_test.append(description_g1 + polygon[22] + "; " + description_l2 + polygon[8])
direction_test.append(description_g1 + polygon[22] + "; " + description_p2 + polygon[3])
direction_test.append(description_p1 + polygon[5] + "; " + description_l2 + polygon[8])
direction_test.append(description_l1 + polygon[8] + "; " + description_g2 + polygon[16])
direction_test.append(description_g1 + polygon[27] + "; " + description_p2 + polygon[5])
direction_test.append(description_g1 + polygon[25] + "; " + description_l2 + polygon[12])
direction_test.append(description_g1 + polygon[31] + "; " + description_l2 + polygon[11])
direction_test.append(description_l1 + polygon[11] + "; " + description_g2 + polygon[16])

direction_test.append(description_p1 + polygon[3] + "; " + description_p2 + polygon[7])
direction_test.append(description_p1 + polygon[2] + "; " + description_p2 + polygon[6])
direction_test.append(description_g1 + polygon[32] + "; " + description_g2 + polygon[33])
direction_test.append(description_g1 + polygon[24] + "; " + description_g2 + polygon[25])

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
    for i in range(24):
        coordinate=direction_test[i]
        prompt = f"""
        Your task is to determine the orientation relation between two closed {Expression} in the same coordinate system.
        Specifically, determine in what orientation y is in x.
        The eight kind of orientation relations will be delimited with ``` tag.
        ```{relation_dir}```.
        The two {Expression} are points or lines or polygons that will be given their position by coordinates: {coordinate}.
        Points are given a coordinate. Lines and polygons are given the coordinates of each vertex in order, where the polygon will eventually return to the first coordinate, drawing the closed figure.
        """
        response = get_completion(prompt)
elif Prompt == "GP":
    for i in range(24):
        coordinate=direction_test[i]
        prompt = f"""
        Your task is to determine the orientation relation between two closed {Expression} in the same coordinate system.
        Specifically, determine in what orientation y is in x.
        The eight kind of orientation relations will be delimited with ``` tag.
        ```{relation_dir}```.
        The two {Expression} are points or lines or polygons that will be given their position by coordinates: {coordinate}.
        Points are given a coordinate. Lines and polygons are given the coordinates of each vertex in order, where the polygon will eventually return to the first coordinate, drawing the closed figure.
        Pay attention to the following points in responding:
        (1) - Compare the range of x and y coordinates occupied by the two {Expression}, don't just focus on one side of the coordinate.
        (2) - If most of the x or y coordinate ranges of two {Expression} overlap, the ranges can be roughly considered to coincide in that coordinate. 
        """
        response=get_completion(prompt)
elif Prompt == "EP":
    for i in range(24):
        coordinate=direction_test[i]
        prompt = f"""
        Your task is to determine the orientation relation between two closed {Expression} in the same coordinate system.
        Specifically, determine in what orientation y is in x.
        The eight kind of orientation relations will be delimited with ``` tag.
        ```{relation_dir}```.
        You will be given two cases to learn how to reason the quesion out. 
        Case 1 - The two {Expression} are points or lines or polygons that will be given their position by coordinates: polygon x: (5,11), (10,11), (10,15), (5,15), (5,11); polygon y: (4,1), (9,1), (9,7), (4,7), (4,1).
        Answer 1 - Based on the given coordinate information, the position of the two circles in the coordinate system can be determined: 
        rectangle x: x-coordinate ranges from 5 to 10, y-coordinate ranges from 11 to 15.
        rectangle y: x coordinate ranges from 4 to 9, y coordinate ranges from 1 to 7.
        Next, reason about the orientation relation between two rectangles:
        (1) The x-coordinate ranges of the two rectangles overlap so much that it can be roughly assumed that the two have the same range in x-coordinate.
        (2) The y-coordinate ranges of the two rectangles do not overlap at all, and the y-coordinate of polygon y is smaller than polygon x. It can be assumed that y is below x.
        Therefore, it is concluded that the two rectangles are Down(x,y).

        Case 2 - The two {Expression} are points or lines or polygons that will be given their position by coordinates: polygon x: (11,0), (16,0), (16,5), (11,5), (11,0); polygon y: (17,7), (21,7), (21,12), (17,12), (17,7).
        Answer 2 - Based on the given coordinate information, the position of the two rectangles in the coordinate system can be determined: 
        rectangle x: x-coordinate ranges from 11 to 16, y-coordinate ranges from 0 to 5.
        rectangle y: x coordinate ranges from 17 to 21, y coordinate ranges from 7 to 12.
        Next, reason about the orientation relation between two rectangles:
        (1) The x-coordinate ranges of the two rectangles do not overlap at all, and the x-coordinate of polygon y is greater than polygon x. It can be assumed that y is to the right of x.
        (2) The y-coordinate ranges of the two rectangles do not overlap at all, and the y-coordinate of polygon y is greater than polygon x. It can be assumed that y is above x.
        Therefore, it is concluded that the two rectangles are Upper Right(x,y).

        Question - The two {Expression} are points or lines or polygons that will be given their position by coordinates: {coordinate}.
        Points are given a coordinate. Lines and polygons are given the coordinates of each vertex in order, are points or lines or polygons that will be given their position by coordinateswhere the polygon will eventually return to the first coordinate, drawing the closed figure.
        """
        response=get_completion(prompt)