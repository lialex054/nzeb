def main():
    print("Running heat_transfer.py")

    layers_dict = {
        'timber_flooring': 0.02,
        'air_gap': 1,
        'plasterboard': 0.01,
    }

    # Set variables
    inside_temp = 23
    outside_temp = 10
    outside_surface = 14.0
    inside_surface = 3.0
    air_gap = 1.4

    material_conductivity = {
            "brick_inner": 0.62,
            "brick_outer": 0.84,
            "glass_fibre_quilt": 0.04,
            "concrete": 1.4,
            "plaster": 0.26,
            "plasterboard": 0.16,
            "plywood": 0.14,
            "roofing_tiles": 0.84,
            "timber_flooring": 0.14,
            "glass": 1.05,
            "air_gap_windows": 0.025,
            "air_gap": None,
            "polyurethane": 0.02,
            "argon": 0.018,
            "krypton": 0.0094
        }

    def find_material(material):
        return material_conductivity[material]

    def layering(material, width):
        coeff = find_material(material)
        layer_val = width/coeff
        return layer_val
    
    def combine_layers(layers):
        combined_value = 0
        for layer in layers:
            if layer == "air_gap":
                combined_value += (1/air_gap)*layers["air_gap"]
            else:
                material = layer
                width = layers[layer]
                combined_value += layering(material, width)
        return combined_value
    
    def heat_flux(layer_vals):
        q = (inside_temp - outside_temp)/((1/outside_surface)+(1/inside_surface)+layer_vals)
        return q
    
    def program_initialise():
        mat_name = layer_material()
        width = layer_width()
        layers_dict[mat_name] = width
        next_layer_bool = input("Would you like to add another layer?: \n")
        if next_layer_bool == 'y' or next_layer_bool == 'Y':
            program_initialise()

    
    def layer_material():
        material_list = []
        for layer in material_conductivity:
            material_list.append(layer)
        print(material_list)
        mat_name = input("What is the material name?: \n")

        if mat_name not in material_list:
                print("Material not in materials list. \n")
                layer_material()
        else:
            return mat_name

    def layer_width():
        width = float(input("What is material width?: \n"))
        return width

    # program_initialise()
    vals = combine_layers(layers_dict)
    final_val = heat_flux(vals)
    print("Your final heat flux is: " + str(final_val))

if __name__ == "__main__":
    main()