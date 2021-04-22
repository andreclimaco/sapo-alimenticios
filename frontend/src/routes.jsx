import React from "react";
import { BrowserRouter, Route, Redirect, Switch } from "react-router-dom";

import TableFoods from "./features/tableFoods/TableFoods";

const Routes = (props) => (
    <BrowserRouter>
        <Switch>
            <Route path="/home" component={TableFoods} />
            <Route path="/proteinas" component={TableFoods} />
            <Route path="/carboidratos" component={TableFoods} />
            <Route path="/gorduras" component={TableFoods} />
            <Redirect from="*" to="/home" />
        </Switch>
    </BrowserRouter>
);

export default Routes;
