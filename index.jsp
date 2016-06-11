<!DOCTYPE html>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="spring" uri="http://www.springframework.org/tags" %>
<html lang="en">


<head>
    <meta>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css"
          integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
    </meta>
</head>

<body>
<div class="container">

    <!-- Static navbar -->
    <nav class="navbar navbar-default">
        <div class="container-fluid">
            <div class="navbar-header">
                <h1>Asociacni pravidla</h1>
            </div>
        </div><!--/.container-fluid -->
    </nav>

    <!-- Main component for a primary marketing message or call to action -->
    <div class="jumbotron">
        <div class="row">
            <div class="col-md-4">
                <label>Antecedent</label>
                <select>
                    <option value="o_delivery_price$UNDEF_0">Cena dodavky - 0</option>
                    <option value="o_delivery_price$1_50">Cena dodavky - 1 az 50</option>
                    <option>Dimenze troll3</option>
                    <option>Dimenze troll4</option>
                </select>
            </div>
            <div class="col-md-4">
                <label>Sukcedent</label>
                <select>
                    <option>Dimenze troll1</option>
                    <option>Dimenze troll2</option>
                    <option>Dimenze troll3</option>
                    <option>Dimenze troll4</option>
                </select>
            </div>
            <div class="col-md-2">
                <label>Plati z:</label>
                <select>
                    <option>99%</option>
                    <option>95%</option>
                    <option>90%</option>
                    <option>75%</option>
                </select>
            </div>
            <div class="col-md-2">
                <label>Plati pro:</label>
                <select>
                    <option>1%</option>
                    <option>5%</option>
                    <option>10%</option>
                    <option>25%</option>
                </select>
            </div>
        </div>
        <div class="row" style="padding-top: 20px">
            <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean bibendum congue erat, quis bibendum nisi
                vestibulum a. Curabitur a hendrerit mauris. Nam varius ornare tristique. Aliquam rhoncus vitae diam et
                congue. Integer urna leo, tristique nec neque laoreet, suscipit commodo lacus. Maecenas sollicitudin
                varius sem in imperdiet. Maecenas erat enim, sagittis ac mattis ut, porttitor sed lectus. Nunc sit amet
                odio leo. Suspendisse congue quam at quam congue semper. Cras tellus lorem, ullamcorper ac pretium nec,
                cursus et augue.
            </p>
            <p>
                Nulla finibus luctus hendrerit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quis
                nulla metus. Suspendisse dolor mauris, vulputate vel mattis et, rhoncus nec felis. Etiam suscipit purus
                lacinia, efficitur elit nec, sagittis ligula. Pellentesque id laoreet nisi. Nullam ac nunc eu sapien
                scelerisque fermentum. Pellentesque condimentum nisl vel tortor luctus blandit. Cras in elit aliquam,
                suscipit libero ut, varius risus. Donec ut nunc tristique, sollicitudin neque vel, aliquet tellus.
                Aenean pretium nisi ac placerat semper. Praesent efficitur consectetur enim, non ullamcorper justo
                tincidunt a. Vestibulum eget metus a diam feugiat faucibus ac in eros. Quisque eget pulvinar nulla.
            </p>
            <p>
                Proin nec ante eget turpis sollicitudin viverra. Sed at enim id nisl porttitor mollis ac sit amet elit.
                Etiam ut facilisis lorem, at porttitor libero. In eleifend quam at mauris mattis molestie. Vivamus
                lobortis cursus elit. Pellentesque ultricies elit nec elit varius aliquam. Suspendisse eget dui augue.
            </p>
        </div>
    </div>

</div>
</body>

</html>
