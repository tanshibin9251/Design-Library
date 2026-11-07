<?php
// Design Library — entry point. Serves the app shell with the library index inlined; template pages load from /api/.
declare(strict_types=1);
$root = __DIR__;
$manifestFile = $root . '/data/manifest.json';
$shellFile = $root . '/includes/shell.html';
if (!is_file($manifestFile) || !is_file($shellFile)) {
    http_response_code(500);
    header('Content-Type: text/plain; charset=utf-8');
    exit("Design Library: data files are missing. Upload the whole folder (data/, includes/, assets/, api/), or run: python build/build.py");
}
$cssV = (string) @filemtime($root . '/assets/app.css');
$jsV  = (string) @filemtime($root . '/assets/app.js');
$etag = '"dl-' . filemtime($manifestFile) . '-' . $cssV . '-' . $jsV . '"';
header('ETag: ' . $etag);
header('Cache-Control: no-cache');
if (($_SERVER['HTTP_IF_NONE_MATCH'] ?? '') === $etag) { http_response_code(304); exit; }
header('Content-Type: text/html; charset=utf-8');
header('X-Content-Type-Options: nosniff');
header('Referrer-Policy: strict-origin-when-cross-origin');
header('X-Frame-Options: SAMEORIGIN');
if (extension_loaded('zlib') && !ini_get('zlib.output_compression')) { ob_start('ob_gzhandler'); }
echo strtr((string) file_get_contents($shellFile), [
    '{{CSS_V}}' => $cssV,
    '{{JS_V}}'  => $jsV,
    '{{DATA}}'  => (string) file_get_contents($manifestFile),
]);
