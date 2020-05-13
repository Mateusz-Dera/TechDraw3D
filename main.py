from extruder.svg import SVG


if __name__ == '__main__':
    file_object  = open("extruder/iw.svg", "r") 

    print(file_object)
    
    # import pdb; pdb.set_trace()
    svgObj = SVG()

    res = svgObj.create_svg_object("extruder/iw.svg")

    print(res)
    a, b, c = svgObj.parse_svg_dict(res)

    print("\n" + str(b))
