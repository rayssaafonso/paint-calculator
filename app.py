from flask import Flask, render_template, request

app = Flask(__name__)

# página index
@app.route('/')
def index():
    return render_template("walls.html")

# página de medidas
@app.route('/measurements', methods=['GET'])
def measurements():
    walls = data_walls(request.args.get("walls"))
    return render_template("measurements.html", walls=walls)

# página de resultados
@app.route('/results', methods=['POST'])
def results():
    data = request.values
    number_data = int(len(data) / 4)
    all_data = []
    total_liters = 0
    total_square_meters = 0

    # loop para chamadas das funções
    for wall in range(int(number_data)):
        data_format = extract_wall_info(data, wall)
        data_format['meters_full'] = calculate_meters(data_format['height'], data_format['width'])
        data_format['windows'] = calculate_windows(data_format['window'])
        data_format['doors'] = calculate_doors(data_format['door'])
        data_format['meters_subtracted'] = subtract_windows_doors(data_format['windows'], data_format['doors'], data_format['meters_full'])
        data_format['walls_rules'] = check_rules(data_format['meters_subtracted'], data_format['windows'], data_format['doors'], data_format['height'])
        data_format['liters'] = calculate_liters(data_format['walls_rules'])
        data_format['wall'] = wall + 1
        total_liters += calculate_liters(data_format['walls_rules'])
        total_liters = round(total_liters, 2)
        total_square_meters += check_rules(data_format['meters_subtracted'], data_format['windows'], data_format['doors'], data_format['height'])
        total_square_meters = round(total_square_meters, 2)
        cans_required = calculate_cans(total_liters)
        all_data.append(data_format)
    return render_template(
        "results.html",
        all_data=all_data,
        total_liters=total_liters,
        total_square_meters=total_square_meters,
        cans_required=cans_required
    )

# função para calcular metros quadrados
def calculate_meters(height, width):
    wall_space = float(height) * float(width)
    return wall_space

# função para calcular espaço das janelas
def calculate_windows(window):
    windows_space = []
    window_size = 2.00 * 1.20
    windows = int(window)
    if windows > 0:
        for i in range(windows):
            windows_space.append(window_size)
    windows_space = float(sum(windows_space))
    return round(windows_space, 2)

# função para calcular espaço das portas
def calculate_doors(door):
    doors_space = []
    door_size = 0.80 * 1.90
    doors = int(door)
    if doors > 0:
        for i in range(doors):
            doors_space.append(door_size)
    doors_space = float(sum(doors_space))
    return round(doors_space, 2)

# diminuir o tamanho das portas e janelas do espaço total
def subtract_windows_doors(windows, doors, meters_full):
    wall_space = meters_full - (windows + doors)
    return round(wall_space, 2)

# validar regras de negócio
def check_rules(meters_full, windows, doors, height):
    available_space = meters_full / 2
    wall_space = meters_full
    if wall_space < 1 or wall_space > 15:
        wall_space = 0.0
    if float(height) < 2.20:
        wall_space = 0.0
    if available_space < (windows + doors):
        wall_space = 0.0
    return round(wall_space, 2)

# função para calcular litros necessários
def calculate_liters(meters_subtracted):
    liters = round(float(meters_subtracted) / 5, 2)
    return liters

# retorno os dados como float
def data_walls(input):
    return float(input)

# função para calcular quantidade de latas necessárias
def calculate_cans(total_liters):
    can_sizes = {
        1: 18.0,
        2: 3.6,
        3: 2.5,
        4: 0.5
    }
    cans = []
    liters = total_liters
    while liters > 0.0:
        if liters <= can_sizes[4]:
            cans.append(can_sizes[4])
            liters = round(liters - can_sizes[4], 2)
        elif liters == can_sizes[1] or liters > can_sizes[1]:
            cans.append(can_sizes[1])
            liters = round(liters - can_sizes[1], 2)
        elif liters == can_sizes[2] or liters > can_sizes[2]:
            cans.append(can_sizes[2])
            liters = round(liters - can_sizes[2], 2)
        elif liters == can_sizes[3] or liters > can_sizes[3]:
            cans.append(can_sizes[3])
            liters = round(liters - can_sizes[3], 2)
        elif liters > can_sizes[4]:
            cans.append(can_sizes[4])
            liters = round(liters - can_sizes[4], 2)
    print(cans)
    can1 = cans.count(can_sizes[1])
    can2 = cans.count(can_sizes[2])
    can3 = cans.count(can_sizes[3])
    can4 = cans.count(can_sizes[4])
    result = []
    if can1 > 0:
        result.append("{} lata(s) de {}L".format(can1, can_sizes[1]))
    if can2 > 0:
        result.append("{} lata(s) de {}L".format(can2, can_sizes[2]))
    if can3 > 0:
        result.append("{} lata(s) de {}L".format(can3, can_sizes[3]))
    if can4 > 0:
        result.append("{} lata(s) de {}L".format(can4, can_sizes[4]))
    result = ', '.join(result)
    return result

# extrair informações que foram inseridas sobre as paredes
def extract_wall_info(data, wall):
    data_format = {
        'height': data_walls(data.get("height-%d" % wall)),
        'width': data_walls(data.get("width-%d" % wall)),
        'door': data_walls(data.get("door-%d" % wall)),
        'window': data_walls(data.get("window-%d" % wall))
    }
    return data_format

if __name__ == '__main__':
    app.run(debug=True)
