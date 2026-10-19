# Baseline Verification

Prefer repository-native commands when available:

- Composer/package graph: `composer validate`, `composer install`,
  `composer show`, `composer dump-autoload`.
- Laravel app: `php artisan about`, `php artisan route:list`,
  `php artisan migrate --pretend` when safe, package install commands.
- Monorepo/workspace when present: `composer run validate:repo`,
  `composer run lint:changed`, package PHPUnit suites.
- REST/OpenAPI: route list, Swagger generation/tests, 401/403/2xx access checks.
- UI/admin/Docara: browser smoke when a runnable target exists.
- SitePack: Node/PHP validators from `repo://sitepack` when inspecting
  `.sitepack` packages.

If checks cannot run, report why and provide the closest safe static
verification.
