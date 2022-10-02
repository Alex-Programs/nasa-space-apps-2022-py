const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const textureLoader = new THREE.TextureLoader();
const geometry = new THREE.SphereGeometry(2, 64, 32);
const map = textureLoader.load("/assets/earthmap1k.jpg");
const bumpMap = textureLoader.load("/assets/earthbump1k.jpg")
const specularMap = textureLoader.load("/assets/earthspecular1k.jpg")
const specular  = new THREE.Color('grey')
const material = new THREE.MeshPhongMaterial({ map, bumpMap, bumpScale: 0.2, specularMap, specular, specular });
const cube = new THREE.Mesh(geometry, material);
scene.add(cube);
const light = new THREE.AmbientLight( 0xA0A0A0 );
const point = new THREE.DirectionalLight(0xffffff, 0.5);
scene.add(light)
scene.add(point)

camera.position.z = 5;

function animate() {
    requestAnimationFrame(animate);

    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;

    renderer.render(scene, camera);
};

animate();