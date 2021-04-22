import { configureStore } from "@reduxjs/toolkit";
import { combineReducers } from "redux";
import foods from "../features/tableFoods/tablefoodsSlice";

const reducer = combineReducers({
    foods,
});

export const store = configureStore({
    reducer,
});
