console.log("LOADED")

const scene2 = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, 1, 0.1, 1000);

const renderer = new THREE.WebGLRenderer({ alpha: true });
renderer.setClearColor( 0xffffff, 0);
renderer.setSize(512, 512);
document.getElementById("three-earth").appendChild(renderer.domElement);

const textureLoader = new THREE.TextureLoader();
const geometry = new THREE.SphereGeometry(2.5, 64, 32);
const map = textureLoader.load("/assets/earthmap8k.jpg");
const bumpMap = textureLoader.load("/assets/earthbump2k.jpg")
const specularMap = textureLoader.load("/assets/earthspecular1k.jpg")
const specular  = new THREE.Color('grey')
const material = new THREE.MeshPhongMaterial({ map, bumpMap, bumpScale: 0.2, specularMap, specular, specular });
const cube = new THREE.Mesh(geometry, material);
scene2.add(cube);
const light = new THREE.AmbientLight( 0xA0A0A0 );
const point = new THREE.DirectionalLight(0xffffff, 0.5);
scene2.add(light)
scene2.add(point)

camera.position.z = 5;

function deg_to_rad(val) {
    return val * (Math.PI / 180)
}

let targetLat = 0
let targetLong = 360

function setLatLong(lat, long) {
    targetLat = lat;
    targetLong = -long + 270;
}

// x axis is latitude, y axis is longitude
function animate() {
    requestAnimationFrame(animate);

    cube.rotation.x -= (cube.rotation.x - deg_to_rad(targetLat)) * 0.05
    cube.rotation.y -= (cube.rotation.y - deg_to_rad(targetLong)) * 0.05
    // if (-(cube.rotation.x - deg_to_rad(targetLong)) < 0.0001) {
    //     targetLat += Math.random() * 90
    //     targetLong += Math.random() * 90
    // }

    renderer.render(scene2, camera);
}

animate();

let params2 = new Proxy(new URLSearchParams(window.location.search), {
    get: (searchParams, prop) => searchParams.get(prop),
  });
  
setLatLong(parseFloat(params2.lat), parseFloat(params2.lon))