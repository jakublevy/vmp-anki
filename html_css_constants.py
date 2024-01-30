front_template = """
    <div class="wrapper rounded shadow">
        <div class="foreign">
            <span>{{question}}</span>
        </div>

        <div class="questionNumber">
            <span>{{question_num}}</span>
        </div>

        <figure class="img">{{question_img}}</figure>

        <div class="native"> a) {{a}}</div>
        <figure class="img">{{a_img}}</figure>

        <div class="native"> b) {{b}}</div>
        <figure class="img">{{b_img}}</figure>

        <div class="native"> c) {{c}}</div>
        <figure class="img">{{c_img}}</figure>
    </div>
    """

back_template = """
    <div class="wrapper rounded shadow">
        <div class="foreign">
            <span>{{question}}</span>
        </div>

        <div class="questionNumber">
            <span>{{question_num}}</span>
        </div>

        <figure class="img">{{question_img}}</figure>

        <div class="native {{a_correct}}"> a) {{a}}</div>
        <figure class="img {{a_correct}}_fig">{{a_img}}</figure>

        <div class="native {{b_correct}}"> b) {{b}}</div>
        <figure class="img {{b_correct}}_fig">{{b_img}}</figure>

        <div class="native {{c_correct}}"> c) {{c}}</div>
        <figure class="img {{c_correct}}_fig">{{c_img}}</figure>
    </div>
    """

styling = """
    .img img,
    .shadow {
      box-shadow: 5px 6px 5px 0px rgba(0,0,0,0.68); 
     }
    body { /* Hack to display background img on ankiuser.net */
      background-color: unset;
    }

    #backgroundImg {
    /*.card:after {*/

      content: ' ';
      display: block;
      position: absolute;
      left: 0;
      top: 0;
      overflow: hidden;
      width: 99%;
      height: 97%;
      z-index: -1;
      opacity: 0.8;  
      background-repeat: no-repeat;
      background-position: 50% 0;
      -ms-background-size: cover;
      -o-background-size: cover;
      -moz-background-size: cover;
      -webkit-background-size: cover;
      background-size: cover;

    }

    .card {
      background-color: transparent;
      position: unset;
    }

     .wrapper {
       padding: 10px;
       margin: 10px;
       display: -webkit-box;
       display: -webkit-flex;
       display: -ms-flexbox;
       display: flex;	
       -webkit-flex-flow: row wrap;	
           -ms-flex-flow: row wrap;	
               flex-flow: row wrap;
       -webkit-box-align: center;
       -webkit-align-items: center;
           -ms-flex-align: center;
               align-items: center;
       /*background-color: #d0d0d0e0; */
        background-color: #000;
       color: #fff;
       font-family: Helvetica;
       font-size: 1.5em;
       font-weight: bold;
       line-height: 26px;
       text-align: left;
    /*   text-shadow: 2px 2px 3px  #121f1fee, -1px 0 10px #ffffffaf;    */
     }

    .img {
     text-align: center;
    }

     .wrapper > * {
       -webkit-box-flex: 1;
       -webkit-flex: 1 100%;
           -ms-flex: 1 100%;
               flex: 1 100%;

       margin: 5px;

     }


     .foreign {  
      /* color:rgb(255, 50, 50); */
      color:#CCCCCC;
      z-index: 1;   
     }

     .native {   
     /*  color:rgb(50, 255, 50); */
        color: goldenrod;

     }


     .correct {
       font-size: 1.5em;
       line-height: 1.2;
       #text-transform: uppercase;
     }

     .wrong {
       font-size: 0.8em;
       font-weight: normal;
       color: #0000;
     }
     
     .correct_fig {
        visibility: visible;
     }
     
     .wrong_fig {
        visibility: hidden;  
     }


     .rounded {
       border-radius: 18px;
       -moz-border-radius: 18px;
       -webkit-border-radius: 18px;
       border: 0px solid #000000;   
     }


     .questionNumber {    
         position: absolute;
         right: 40px;
         top: 40px;
       }

     @media all and (max-height: 400px) {

       .img img {
        width: 20%;
       }
      .wrapper, #hintButton {
        font-size: 80%;    
        line-height: 16px;
      }

     }


     @media all and (min-width: 400px) {
       .native1, .native2 {
         -webkit-box-flex: 1;
         -webkit-flex: 1 auto;
             -ms-flex: 1 auto;
                 flex: 1 auto;  
       /*  background-color: #ff0040e8; */
       } 
 }
    """