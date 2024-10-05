def add_movement(movement_type: str, amount: float, category: str, description:str):
    movement = {
        "type": movement_type,
        "title": description,
        "amount": amount,
        "category": category
    }
    return movement