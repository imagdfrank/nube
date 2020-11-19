Vue.component('navegador', {
    template: `    
    <nav class="navbar navbar-expand-md navbar-dark bg-dark navbar-fixed-top">
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
        </button>
            <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
        
                <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
                    <li class="nav-item active">
                        <a class="nav-link" href="Index.html">Inicio <span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="proyectos.html">Proyectos</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="ayuda.html" >Ayuda</a>
                    </li>
                </ul>
                
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="ingresar.html"> Ingresar</a></li>
                    <li><a href="registro.html"> Registrarse</a></li>
                </ul>
            </div>
    </nav> 
    `
})

Vue.component('otropie', {
    template: `    
        <div>
        <!-- Footer -->
        <footer class="page-footer font-small mdb-color lighten-3 pt-4">
        
          <!-- Footer Elements -->
          <div class="container">
        
            <!--Grid row-->
            <div class="row">
        
              <!--Grid column-->
              <div class="col-lg-2 col-md-12 mb-4">
        
                <!--Image-->
                <div class="view overlay z-depth-1-half">
                  <img src="https://juanmariasolare.files.wordpress.com/2018/12/El-sistema-tonal-como-sistema-planetario.jpg?w=1044&h=561&crop=1" class="img-fluid"
                    alt="">
                  <a href="">
                    <div class="mask rgba-white-light"></div>
                  </a>
                </div>
        
              </div>
              <!--Grid column-->
        
              <!--Grid column-->
              <div class="col-lg-2 col-md-6 mb-4">
        
                <!--Image-->
                <div class="view overlay z-depth-1-half">
                  <img src="https://i0.wp.com/blogthinkbig.com/wp-content/uploads/2019/07/hand-3685829_1920-e1563532758880.jpg?resize=610%2C225&ssl=1" class="img-fluid"
                    alt="">
                  <a href="">
                    <div class="mask rgba-white-light"></div>
                  </a>
                </div>
        
              </div>
              <!--Grid column-->
        
              <!--Grid column-->
              <div class="col-lg-2 col-md-6 mb-4">
        
                <!--Image-->
                <div class="view overlay z-depth-1-half">
                  <img src="https://www.compartirpalabramaestra.org/sites/default/files/styles/articulos/public/field/image/por-que-es-tan-dificil-aprender-ciencias-sociales.jpg?itok=VskSRCNV" class="img-fluid"
                    alt="">
                  <a href="">
                    <div class="mask rgba-white-light"></div>
                  </a>
                </div>
        
              </div>
              <!--Grid column-->
        
              <!--Grid column-->
              <div class="col-lg-2 col-md-12 mb-4">
        
                <!--Image-->
                <div class="view overlay z-depth-1-half">
                  <img src="https://forococheselectricos.com/wp-content/uploads/2019/11/Tesla-Cybertruck-1.png" class="img-fluid"
                    alt="">
                  <a href="">
                    <div class="mask rgba-white-light"></div>
                  </a>
                </div>
        
              </div>
              <!--Grid column-->
        
              <!--Grid column-->
              <div class="col-lg-2 col-md-6 mb-4">
        
                <!--Image-->
                <div class="view overlay z-depth-1-half">
                  <img src="https://rockcontent.com/es/wp-content/uploads/2019/02/principios-de-la-redaccion-web-1280x720.png" class="img-fluid"
                    alt="">
                  <a href="">
                    <div class="mask rgba-white-light"></div>
                  </a>
                </div>
        
              </div>
              <!--Grid column-->
        
              <!--Grid column-->
              <div class="col-lg-2 col-md-6 mb-4">
        
                <!--Image-->
                <div class="view overlay z-depth-1-half">
                  <img src="https://www.nibcode.com/images/contents/1135/primary.png" class="img-fluid"
                    alt="">
                  <a href="">
                    <div class="mask rgba-white-light"></div>
                  </a>
                </div>
        
              </div>
              <!--Grid column-->
        
            </div>
            <!--Grid row-->
        
          </div>
          <!-- Footer Elements -->
        
          <!-- Copyright -->
          <div class="footer-copyright text-center py-3">© 2020 Copyright
          </div>
          <!-- Copyright -->
        
        </footer>
        <!-- Footer -->
        </div> 
    `
})

new Vue({
    el: '#app',

    computed: {
        mystyle: function() {
            return {
                height: '15vh'
            }
        }
    }
})

