import axios from "axios";

export function api(navPath) {
    let clientAPI = axios.create({
        baseURL: "http://localhost:9000/api/",
        headers: {
            "Content-Type": "application/json",
        },
    });

    let params = {};

    switch (navPath) {
        case "/proteinas":
            params = {
                macronutrients: "proteins",
                ordering: "-proteins,name",
            };
            break;
        case "/carboidratos":
            params = {
                macronutrients: "carbohydrates",
                ordering: "-carbohydrates,name",
            };
            break;
        case "/gorduras":
            params = {
                macronutrients: "fats",
                ordering: "-fats,name",
            };
            break;
        default:
            params = {
                ordering: "-fats,name",
            };
    }
    try {
        return clientAPI.get("/foods/", { params });
    } catch (e) {
        return console.error(e.message);
    }
}
