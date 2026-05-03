# Пример: bootstrap нового Simai-модуля

## Цель
Сделать новый пакет, который ставится через минимум команд.

## Минимальный каркас
- `packages/<module>/composer.json`
- `packages/<module>/module.yaml`
- `packages/<module>/SPEC.md`
- `packages/<module>/CHANGELOG.md`
- `packages/<module>/src/Providers/<Module>ServiceProvider.php`
- `packages/<module>/config/simai_<module>.php`
- `packages/<module>/src/Commands/InstallCommand.php` с сигнатурой `simai:install-<module>`
- `packages/<module>/resources/lang/ru/*.php`
- `packages/<module>/resources/lang/en/*.php`
- `packages/<module>/tests/Feature/*`
- `packages/<module>/tests/Unit/*`

## Правила интеграции
1. Команда установки должна быть идемпотентной и неинтерактивной.
2. Провайдер должен регистрировать команду установки.
3. Операции/доступы/меню должны описываться в `config/simai_<module>.php`.
4. CRUD маршруты создавать через `simaiCrud`/`simaiApiCrud`.
5. Для CRUD действий опираться на `EntityConfig` + `access.entity` проверки.
6. UI страницы строить на `admin::layouts.*` и `admin::crud.*`.
7. При расширении UI добавлять совместимые виджеты/шаблоны через пресеты/драйверы.
8. Локализация: минимум `ru` и `en` с одинаковыми ключами.
9. Без внешних CDN и жестких внешних URL.
10. Все поведенческие изменения покрывать тестами.

## Шаблон команды установки
```php
<?php

namespace Simai\Example\Commands;

use Illuminate\Console\Command;

class InstallExample extends Command
{
    protected $signature = 'simai:install-example';
    protected $description = 'Install example module data';

    public function handle(): int
    {
        // Идемпотентные операции: updateOrCreate/sync* и безопасные повторные вызовы
        // Без интерактивных вопросов
        $this->info('Example module installed');

        return self::SUCCESS;
    }
}
```

## Шаблон регистрации CRUD роутов
```php
Route::prefix('admin')
    ->middleware(['web', 'auth'])
    ->group(function () {
        Route::simaiCrud('example/items', \Simai\Example\Crud\ExampleEntityConfig::class)
            ->param('id')
            ->only(['index', 'show', 'create', 'store', 'edit', 'update', 'destroy'])
            ->names(['ui' => 'admin.example.items'])
            ->register();
    });
```

## Проверка
- `composer run validate:repo`
- `composer run lint:changed`
- `vendor/bin/phpunit packages/<module>/tests`
- Установка в хост-проекте: `composer require simai/<module>` + `php artisan simai:install`
