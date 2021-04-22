import tablefoodsReducer, {
    startLoading,
    hasError,
    foodsSuccess,
} from "./tablefoodsSlice";

describe("coutablefoodsnter reducer", () => {
    const initialState = {
        foods: [],
        isLoading: false,
        error: false,
    };

    it("should handle initial state", () => {
        expect(tablefoodsReducer(undefined, { type: "unknown" })).toEqual({
            foods: [],
            isLoading: false,
            error: false,
        });
    });

    it("should handle startLoading", () => {
        const actual = tablefoodsReducer(initialState, startLoading());
        expect(actual.isLoading).toEqual(true);
    });

    it("should handle hasError", () => {
        const actual = tablefoodsReducer(initialState, hasError());
        expect(actual.isLoading).toEqual(false);
        expect(actual.error).not.toEqual(initialState.error);
    });

    it("should handle foodsSuccess", () => {
        const actual = tablefoodsReducer(initialState, foodsSuccess());
        expect(actual.isLoading).toEqual(false);
        expect(actual.foods).not.toEqual([]);
    });
});
