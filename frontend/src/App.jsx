import React from "react";
import logo from "./logo.svg";
import Routes from "./routes";
import { Container, Row, Col, Navbar, Nav } from "react-bootstrap";
import "./App.css";
import "bootstrap/dist/css/bootstrap.css";

function App() {
    return (
        <Container fluid>
            <Row>
                <Col>
                    <Navbar bg="topo" variant="topo" expand="md">
                        <Navbar.Brand href="/home">
                            <img alt="" src={logo} className="logo" />
                            Home
                        </Navbar.Brand>
                        <Navbar.Toggle aria-controls="basic-navbar-nav" />
                        <Navbar.Collapse
                            className="collapse navbar-collapse justify-content-end"
                            id="basic-navbar-nav"
                        >
                            <Nav
                                className="navbar-nav pr-3"
                                activeKey={window.location.pathname}
                            >
                                <Nav.Link href="/proteinas">Proteínas</Nav.Link>
                                <Nav.Link href="/carboidratos">
                                    Carboidratos
                                </Nav.Link>
                                <Nav.Link href="/gorduras">Gorduras</Nav.Link>
                            </Nav>
                        </Navbar.Collapse>
                    </Navbar>
                </Col>
            </Row>
            <Container bsPrefix="main-content">
                <Row>
                    <Col>
                        <Container bsPrefix="description-site">
                            <h1>
                                Bem-vindo ao <i>Sapo Alimentício</i>, aqui você
                                irá encontrar informações nutricionais dos
                                principais alimentos do mercado.
                            </h1>
                        </Container>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <Container bsPrefix="table-responsive table-foods">
                            <Routes />
                        </Container>
                    </Col>
                </Row>
            </Container>
        </Container>
    );
}

export default App;
