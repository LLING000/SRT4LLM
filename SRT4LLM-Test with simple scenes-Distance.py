Expression_list=["regions","geometrical shapes"]
Expression=Expression_list[0] # choose the "expression" dimension

Shape_list=["rectangles","circles"]
Shape=Shape_list[0]

Prompt_list=["SP","GP","EP"]
Prompt=Prompt_list[0]

# rectangle-distance relation
distance_rec=[]
# Group 1
distance_rec.append("(12,14), (13,14), (13,15), (12,15), (12,14)")
distance_rec.append("(12,18), (13,18), (13,19), (12,19), (12,18)")
distance_rec.append("(12,24), (13,24), (13,25), (12,25), (12,24)")
# Group 2
distance_rec.append("(13.5,13.5), (14.5,13.5), (14.5,14.5), (13.5,14.5), (13.5,13.5)")
distance_rec.append("(16,16), (17,16), (17,17), (16,17), (16,16)")
distance_rec.append("(20,20), (21,20), (21,21), (20,21), (20,20)")
# Group 3
distance_rec.append("(14,12), (15,12), (15,13), (14,13), (14,12)")
distance_rec.append("(18,12), (19,12), (19,13), (18,13), (18,12)")
distance_rec.append("(24,12), (25,12), (25,13), (24,13), (24,12)")
# Group 4
distance_rec.append("(13.5,10.5), (14.5,10.5), (14.5,11.5), (13.5,11.5), (13.5,10.5)")
distance_rec.append("(16,8), (17,8), (17,9), (16,9), (16,8)")
distance_rec.append("(20,4), (21,4), (21,5), (20,5), (20,4)")
# Group 5
distance_rec.append("(12,10), (13,10), (13,11), (12,11), (12,10)")
distance_rec.append("(12,6), (13,6), (13,7), (12,7), (12,6)")
distance_rec.append("(12,0), (13,0), (13,1), (12,1), (12,0)")
# Group 6
distance_rec.append("(10.5,10.5), (11.5,10.5), (11.5,11.5), (10.5,11.5), (10.5,10.5)")
distance_rec.append("(8,8), (9,8), (9,9), (8,9), (8,8)")
distance_rec.append("(4,4), (5,4), (5,5), (4,5), (4,4)")
# Group 7
distance_rec.append("(10,12), (11,12), (11,13), (10,13), (10,12)")
distance_rec.append("(6,12), (7,12), (7,13), (6,13), (6,12)")
distance_rec.append("(0,12), (1,12), (1,13), (0,13), (0,12)")
# Group 8
distance_rec.append("(10.5,13.5), (11.5,13.5), (11.5,14.5), (10.5,14.5), (10.5,13.5)")
distance_rec.append("(8,16), (9,16), (9,17), (8,17), (8,16)")
distance_rec.append("(4,20), (5,20), (5,21), (4,21), (4,20)")

# circle-distance relation
distance_cir=[]
# Group 1
distance_cir.append("O:(13,15), r=0.5")
distance_cir.append("O:(13,19), r=0.5")
distance_cir.append("O:(13,25), r=0.5")
# Group 2
distance_cir.append("O:(14,14), r=0.5")
distance_cir.append("O:(17,17), r=0.5")
distance_cir.append("O:(21,21), r=0.5")
# Group 3
distance_cir.append("O:(15,13), r=0.5")
distance_cir.append("O:(19,13), r=0.5")
distance_cir.append("O:(25,13), r=0.5")
# Group 4
distance_cir.append("O:(14,12), r=0.5")
distance_cir.append("O:(17,9), r=0.5")
distance_cir.append("O:(21,5), r=0.5")
# Group 5
distance_cir.append("O:(13,11), r=0.5")
distance_cir.append("O:(13,7), r=0.5")
distance_cir.append("O:(13,1), r=0.5")
# Group 6
distance_cir.append("O:(12,12), r=0.5")
distance_cir.append("O:(9,9), r=0.5")
distance_cir.append("O:(5,5), r=0.5")
# Group 7
distance_cir.append("O:(11,13), r=0.5")
distance_cir.append("O:(7,13), r=0.5")
distance_cir.append("O:(1,13), r=0.5")
# Group 8
distance_cir.append("O:(12,14), r=0.5")
distance_cir.append("O:(9,17), r=0.5")
distance_cir.append("O:(5,21), r=0.5")

# The definition of distance relation
relation_dis=f""" 
Qualitatively describe the relation by delimiting the distance range.
    (1) Close(x,y): The length of the distance from x to y is [0,2].
    (2) Medium(x,y): The length of the distance from x to y is (2,6].
    (3) Far(x,y): The length of the distance from x to y is (6,+∞).
"""

def get_completion(prompt):
    # Connect to your LLM to get the response.
    response="LLM Response"
    return response

if Prompt == "SP":
    if Shape == "rectangle":
        for i in range(24):
            dis_y = distance_rec[i]
            distance_rec = "rectangle x: (12,12), (13,12), (13,13), (12,13), (12,12); rectangle y: "+ dis_y
            prompt = f"""
            Your task is to determine the distance relation between two closed {Expression} in the same coordinate system.
            The three kind of distance relations will be delimited with ``` tag.
            ```{relation_dis}```.
            The two {Expression} are {Shape} that will be given their position by coordinates: {distance_rec}.
            """
            response = get_completion(prompt)
    elif Shape == "circle":
        for i in range(24):
            dis_y = distance_cir[i]
            distance_cir = "circle x: O:(13,13), r=0.5; circle y: "+ dis_y
            prompt = f"""
            Your task is to determine the distance relation between two closed {Expression} in the same coordinate system.
            The three kind of distance relations will be delimited with ``` tag.
            ```{relation_dis}```.
            The two {Expression} are {Shape} that will be given their position by the center O and the radius r: {distance_cir}.
            """
            response = get_completion(prompt)
elif Prompt == "GP":
    if Shape == "rectangle":
        for i in range(24):
            dis_y = distance_rec[i]
            distance_rec = "rectangle x: (12,12), (13,12), (13,13), (12,13), (12,12); rectangle y: "+ dis_y
            prompt = f"""
            Your task is to determine the distance relation between two closed {Expression} in the same coordinate system.
            The three kind of distance relations will be delimited with ``` tag.
            ```{relation_dis}```.
            The two {Expression} are {Shape} that will be given their position by coordinates: {distance_rec}.
            Pay attention to the following points in responding:
            (1) - Calculate the distance between the two {Expression} before making a judgment. 
            (2) - In the context of intervals, "(" or ")" means the endpoint is not included, while "[" or "]" means the endpoint is included.
            """
            response = get_completion(prompt)
    elif Shape == "circle":
        for i in range(24):
            dis_y = distance_cir[i]
            distance_cir = "circle x: O:(13,13), r=0.5; circle y: "+ dis_y
            prompt = f"""
            Your task is to determine the distance relation between two closed {Expression} in the same coordinate system.
            The three kind of distance relations will be delimited with ``` tag.
            ```{relation_dis}```.
            The two {Expression} are {Shape} that will be given their position by the center O and the radius r: {distance_cir}.
            Pay attention to the following points in responding:
            (1) - Calculate the distance between the two {Expression} before making a judgment. 
            (2) - In the context of intervals, "(" or ")" means the endpoint is not included, while "[" or "]" means the endpoint is included.
            """
            response = get_completion(prompt)
elif Prompt == "EP":
    if Shape == "rectangle":
        for i in range(24):
            dis_y = distance_rec[i]
            distance_rec = "rectangle x: (12,12), (13,12), (13,13), (12,13), (12,12); rectangle y: "+ dis_y
            prompt = f"""
            Your task is to determine the distance relation between two closed {Expression} in the same coordinate system.
            The three kind of distance relations will be delimited with ``` tag.
            ```{relation_dis}```.
            You will be given two cases to learn how to reason the quesion out. 
            Case 1 - The two {Expression} are {Shape} that will be given their position by coordinates: rectangle x: (4,7), (5,7), (5,8), (4,8), (4,7); rectangle y: (6,7), (7,7), (7,8), (6,8), (6,7).
            Answer 1 - Based on the given coordinate information, the center of the two rectangles in the coordinate system can be determined: 
            rectangle x: x-coordinate is (4+5)/2=4.5, y-coordinate is (7+8)/2=7.5.
            rectangle y: x-coordinate is (6+7)/2=6.5, y-coordinate is (7+8)/2=7.5.
            Next, reason about the distance relation between two rectangles:
            (1) Calculate the distance: d=sqrt((6.5-4.5)^2+(7.5-7.5)^2) = sqrt(4) = 2.
            (2) The distance between the two rectangles is 2 which falls into the interval [0,2].
            Therefore, it is concluded that the two rectangles are Close(x,y).
            
            Case 2 - The two {Expression} are {Shape} that will be given their position by coordinates: rectangle x: (8,2), (9,2), (9,3), (8,3), (8,2); rectangle y: (16,6), (17,6), (17,7), (16,7), (16,6).
            Answer 2 - Based on the given coordinate information, the position of the two rectangles in the coordinate system can be determined: 
            rectangle x: x-coordinate is (8+9)/2=8.5, y-coordinate is (2+3)/2=2.5.
            rectangle y: x-coordinate is (16+17)/2=16.5, y-coordinate is (6+7)/2=6.5.
            Next, reason about the orientation relation between two rectangles:
            (1) Calculate the distance: d=sqrt((16.5-8.5)^2+(6.5-2.5)^2) = sqrt(64+16) = sqrt(80) ≈ 8.944.
            (2) The distance between the two rectangles is approximately 8.944 which falls into the interval (6,+∞).
            Therefore, it is concluded that the two rectangles are Far(x,y).
            
            Question - The two {Expression} are {Shape} that will be given their position by coordinates: {distance_rec}.
            """
            response = get_completion(prompt)
    elif Shape == "circle":
        for i in range(24):
            dis_y = distance_cir[i]
            distance_cir = "circle x: O:(13,13), r=0.5; circle y: "+ dis_y
            prompt = f"""
            Your task is to determine the distance relation between two closed {Expression} in the same coordinate system.
            The three kind of distance relations will be delimited with ``` tag.
            ```{relation_dis}```.
            You will be given two cases to learn how to reason the quesion out. 
            Case 1 - The two {Expression} are {Shape} that will be given their position by the center O and the radius r: circle x: O:(15,4), r=0.5; circle y: O:(9,4), r=0.5.
            Answer 1 - Based on the given coordinate information, the center of the two circles in the coordinate system can be determined: 
            circle x: the center is (15,4), the radii is 0.5.
            circle y: the center is (9,4), the radii is 0.5.
            Next, reason about the distance relation between two circles:
            (1) Calculate the distance: d=sqrt((15-9)^2+(4-4)^2) = sqrt(36) = 6.
            (2) The distance between the two circles is 6 which falls into the interval (2,6].
            Therefore, it is concluded that the two circles are Medium(x,y).
            
            Case 2 - The two {Expression} are {Shape} that will be given their position by the center O and the radius r: circle x: O:(3,10), r=0.5; circle y: O:(8,3), r=0.5.
            Answer 2 - Based on the given coordinate information, the position of the two circles in the coordinate system can be determined: 
            circle x: the center is (3,10), the radii is 0.5.
            circle y: the center is (8,3), the radii is 0.5.
            Next, reason about the orientation relation between two circles:
            (1) Calculate the distance: d=sqrt((8-3)^2+(3-10)^2) = sqrt(25+49) = sqrt(74) ≈ 8.602.
            (2) The distance between the two circles is approximately 8.602 which falls into the interval (6,+∞).
            Therefore, it is concluded that the two circles are Far(x,y).
            
            Question - The two {Expression} are {Shape} that will be given their position by the center O and the radius r: {distance_cir}.
            """
            response = get_completion(prompt)