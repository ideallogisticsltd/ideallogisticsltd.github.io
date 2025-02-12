'use strict';
const MANIFEST = 'flutter-app-manifest';
const TEMP = 'flutter-temp-cache';
const CACHE_NAME = 'flutter-app-cache';

const RESOURCES = {"assets/AssetManifest.bin": "24422d5fa17ea915da8ff56f2e340c29",
"assets/AssetManifest.bin.json": "a94fd4a29f524579c511fffed30afd91",
"assets/AssetManifest.json": "fefef8c081d4b04bc727586d4431467c",
"assets/FontManifest.json": "209e66e2f71c646cc7eb744ea1cea0dc",
"assets/fonts/MaterialIcons-Regular.otf": "fc519719861c60af81d2bbc93cf524b4",
"assets/lib/assets/aboutus/commercialkitchen.jpg": "caef2d73fc044d66b96b52086bf783f1",
"assets/lib/assets/aboutus/experts.jpg": "76038ef8bff3766e437bec6e14ad2e28",
"assets/lib/assets/aboutus/guarantee.jpg": "6e5054f854004fb4b6630856338e5389",
"assets/lib/assets/aboutus/kitchen.jpg": "7bd32c9589ae5852b4ddea00cdbfa20e",
"assets/lib/assets/aboutus/promisetodeliver.jpg": "99a494d33858eeb38c46562a7d3c370e",
"assets/lib/assets/clients/burgerking.jpg": "c669adcbe2bc1a6ffc0bdc2d6a03c98a",
"assets/lib/assets/clients/crowne.jpg": "ca5e80b3bb1d4a26b938424ac7a8ebf0",
"assets/lib/assets/clients/eka.jpg": "4383cadc2874843fd4e18825cf217edd",
"assets/lib/assets/clients/hillcrest.jpg": "163e78ecd781b570a0b89f120f4018fd",
"assets/lib/assets/clients/hilton.jpg": "eb3b6ca75b3d150d985e5237597218eb",
"assets/lib/assets/clients/ibis.jpg": "3299c21cb57532e6e1e532e39f007377",
"assets/lib/assets/clients/java.jpg": "ddb43fdffe71bcd90cd8284278efefef",
"assets/lib/assets/clients/nairobihospital.jpg": "071e33e9a5d543e2b2093147e00cd97c",
"assets/lib/assets/clients/radisson.jpg": "c1186a7e2aed34e9c1ddca0153888dcc",
"assets/lib/assets/clients/strathmore.jpg": "e19701ab806b5eb6b8042b2876378e58",
"assets/lib/assets/icons/90690-shopping.json": "402ec3380515631c80034167d991f6b9",
"assets/lib/assets/icons/glass1.jpg": "1336d3ccf9e5b8aab44518ea144ba627",
"assets/lib/assets/icons/glass2.jpg": "38f4af661191aaebc595674df335c532",
"assets/lib/assets/icons/glass3.jpg": "2e20bb6cbcc9f7e3f55ae52e34efb49d",
"assets/lib/assets/icons/logo.png": "00c118883fa841fc7be3cb65781dbecc",
"assets/lib/assets/products/glass1.jpg": "1336d3ccf9e5b8aab44518ea144ba627",
"assets/lib/assets/products/glass2.jpg": "38f4af661191aaebc595674df335c532",
"assets/lib/assets/products/glass3.jpg": "2e20bb6cbcc9f7e3f55ae52e34efb49d",
"assets/lib/icons/90690-shopping.json": "402ec3380515631c80034167d991f6b9",
"assets/lib/icons/glass1.jpg": "1336d3ccf9e5b8aab44518ea144ba627",
"assets/lib/icons/glass2.jpg": "38f4af661191aaebc595674df335c532",
"assets/lib/icons/glass3.jpg": "2e20bb6cbcc9f7e3f55ae52e34efb49d",
"assets/lib/icons/logo.png": "00c118883fa841fc7be3cb65781dbecc",
"assets/NOTICES": "2e5732decbf5ead184e42d0006d34163",
"assets/packages/awesome_snackbar_content/assets/back.svg": "ba1c3aebba280f23f5509bd42dab958d",
"assets/packages/awesome_snackbar_content/assets/bubbles.svg": "1df6817bf509ee4e615fe821bc6dabd9",
"assets/packages/awesome_snackbar_content/assets/types/failure.svg": "cb9e759ee55687836e9c1f20480dd9c8",
"assets/packages/awesome_snackbar_content/assets/types/help.svg": "7fb350b5c30bde7deeb3160f591461ff",
"assets/packages/awesome_snackbar_content/assets/types/success.svg": "6e273a8f41cd45839b2e3a36747189ac",
"assets/packages/awesome_snackbar_content/assets/types/warning.svg": "cfcc5fcb570129febe890f2e117615e0",
"assets/packages/cupertino_icons/assets/CupertinoIcons.ttf": "e986ebe42ef785b27164c36a9abc7818",
"assets/packages/flutter_charts/google_fonts/Comforter-Regular.ttf": "cff123ea94f9032380183b8bbbf30ec1",
"assets/shaders/ink_sparkle.frag": "ecc85a2e95f5e9f53123dcaf8cb9b6ce",
"canvaskit/canvaskit.js": "26eef3024dbc64886b7f48e1b6fb05cf",
"canvaskit/canvaskit.js.symbols": "efc2cd87d1ff6c586b7d4c7083063a40",
"canvaskit/canvaskit.wasm": "e7602c687313cfac5f495c5eac2fb324",
"canvaskit/chromium/canvaskit.js": "b7ba6d908089f706772b2007c37e6da4",
"canvaskit/chromium/canvaskit.js.symbols": "e115ddcfad5f5b98a90e389433606502",
"canvaskit/chromium/canvaskit.wasm": "ea5ab288728f7200f398f60089048b48",
"canvaskit/skwasm.js": "ac0f73826b925320a1e9b0d3fd7da61c",
"canvaskit/skwasm.js.symbols": "96263e00e3c9bd9cd878ead867c04f3c",
"canvaskit/skwasm.wasm": "828c26a0b1cc8eb1adacbdd0c5e8bcfa",
"canvaskit/skwasm.worker.js": "89990e8c92bcb123999aa81f7e203b1c",
"favicon.png": "00c118883fa841fc7be3cb65781dbecc",
"flutter.js": "4b2350e14c6650ba82871f60906437ea",
"flutter_bootstrap.js": "da68bfde63c549e011db22e3a5c45ae8",
"icons/Icon-192.png": "00c118883fa841fc7be3cb65781dbecc",
"icons/Icon-512.png": "00c118883fa841fc7be3cb65781dbecc",
"icons/Icon-maskable-192.png": "00c118883fa841fc7be3cb65781dbecc",
"icons/Icon-maskable-512.png": "00c118883fa841fc7be3cb65781dbecc",
"index.html": "4c684f8d7234767f05f7eea872d02f95",
"/": "4c684f8d7234767f05f7eea872d02f95",
"main.dart.js": "32e69202017a9942a8a98eb1010958fc",
"manifest.json": "5ab5c68d5e3ac163b3eac229b9e28fd2",
"version.json": "2376e65938d69b06b0bad28ad28ad7b3"};
// The application shell files that are downloaded before a service worker can
// start.
const CORE = ["main.dart.js",
"index.html",
"flutter_bootstrap.js",
"assets/AssetManifest.bin.json",
"assets/FontManifest.json"];

// During install, the TEMP cache is populated with the application shell files.
self.addEventListener("install", (event) => {
  self.skipWaiting();
  return event.waitUntil(
    caches.open(TEMP).then((cache) => {
      return cache.addAll(
        CORE.map((value) => new Request(value, {'cache': 'reload'})));
    })
  );
});
// During activate, the cache is populated with the temp files downloaded in
// install. If this service worker is upgrading from one with a saved
// MANIFEST, then use this to retain unchanged resource files.
self.addEventListener("activate", function(event) {
  return event.waitUntil(async function() {
    try {
      var contentCache = await caches.open(CACHE_NAME);
      var tempCache = await caches.open(TEMP);
      var manifestCache = await caches.open(MANIFEST);
      var manifest = await manifestCache.match('manifest');
      // When there is no prior manifest, clear the entire cache.
      if (!manifest) {
        await caches.delete(CACHE_NAME);
        contentCache = await caches.open(CACHE_NAME);
        for (var request of await tempCache.keys()) {
          var response = await tempCache.match(request);
          await contentCache.put(request, response);
        }
        await caches.delete(TEMP);
        // Save the manifest to make future upgrades efficient.
        await manifestCache.put('manifest', new Response(JSON.stringify(RESOURCES)));
        // Claim client to enable caching on first launch
        self.clients.claim();
        return;
      }
      var oldManifest = await manifest.json();
      var origin = self.location.origin;
      for (var request of await contentCache.keys()) {
        var key = request.url.substring(origin.length + 1);
        if (key == "") {
          key = "/";
        }
        // If a resource from the old manifest is not in the new cache, or if
        // the MD5 sum has changed, delete it. Otherwise the resource is left
        // in the cache and can be reused by the new service worker.
        if (!RESOURCES[key] || RESOURCES[key] != oldManifest[key]) {
          await contentCache.delete(request);
        }
      }
      // Populate the cache with the app shell TEMP files, potentially overwriting
      // cache files preserved above.
      for (var request of await tempCache.keys()) {
        var response = await tempCache.match(request);
        await contentCache.put(request, response);
      }
      await caches.delete(TEMP);
      // Save the manifest to make future upgrades efficient.
      await manifestCache.put('manifest', new Response(JSON.stringify(RESOURCES)));
      // Claim client to enable caching on first launch
      self.clients.claim();
      return;
    } catch (err) {
      // On an unhandled exception the state of the cache cannot be guaranteed.
      console.error('Failed to upgrade service worker: ' + err);
      await caches.delete(CACHE_NAME);
      await caches.delete(TEMP);
      await caches.delete(MANIFEST);
    }
  }());
});
// The fetch handler redirects requests for RESOURCE files to the service
// worker cache.
self.addEventListener("fetch", (event) => {
  if (event.request.method !== 'GET') {
    return;
  }
  var origin = self.location.origin;
  var key = event.request.url.substring(origin.length + 1);
  // Redirect URLs to the index.html
  if (key.indexOf('?v=') != -1) {
    key = key.split('?v=')[0];
  }
  if (event.request.url == origin || event.request.url.startsWith(origin + '/#') || key == '') {
    key = '/';
  }
  // If the URL is not the RESOURCE list then return to signal that the
  // browser should take over.
  if (!RESOURCES[key]) {
    return;
  }
  // If the URL is the index.html, perform an online-first request.
  if (key == '/') {
    return onlineFirst(event);
  }
  event.respondWith(caches.open(CACHE_NAME)
    .then((cache) =>  {
      return cache.match(event.request).then((response) => {
        // Either respond with the cached resource, or perform a fetch and
        // lazily populate the cache only if the resource was successfully fetched.
        return response || fetch(event.request).then((response) => {
          if (response && Boolean(response.ok)) {
            cache.put(event.request, response.clone());
          }
          return response;
        });
      })
    })
  );
});
self.addEventListener('message', (event) => {
  // SkipWaiting can be used to immediately activate a waiting service worker.
  // This will also require a page refresh triggered by the main worker.
  if (event.data === 'skipWaiting') {
    self.skipWaiting();
    return;
  }
  if (event.data === 'downloadOffline') {
    downloadOffline();
    return;
  }
});
// Download offline will check the RESOURCES for all files not in the cache
// and populate them.
async function downloadOffline() {
  var resources = [];
  var contentCache = await caches.open(CACHE_NAME);
  var currentContent = {};
  for (var request of await contentCache.keys()) {
    var key = request.url.substring(origin.length + 1);
    if (key == "") {
      key = "/";
    }
    currentContent[key] = true;
  }
  for (var resourceKey of Object.keys(RESOURCES)) {
    if (!currentContent[resourceKey]) {
      resources.push(resourceKey);
    }
  }
  return contentCache.addAll(resources);
}
// Attempt to download the resource online before falling back to
// the offline cache.
function onlineFirst(event) {
  return event.respondWith(
    fetch(event.request).then((response) => {
      return caches.open(CACHE_NAME).then((cache) => {
        cache.put(event.request, response.clone());
        return response;
      });
    }).catch((error) => {
      return caches.open(CACHE_NAME).then((cache) => {
        return cache.match(event.request).then((response) => {
          if (response != null) {
            return response;
          }
          throw error;
        });
      });
    })
  );
}
