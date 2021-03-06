import random

from fineract.objects.hook import Hook

number = random.randint(0, 10000)


def test_create_hook(fineract):
    events = [
        {
            'actionName': 'DISBURSE',
            'entityName': 'LOAN'
        },
        {
            'actionName': 'REPAYMENT',
            'entityName': 'LOAN'
        }
    ]
    hook = Hook.create_web_hook(fineract.request_handler, 'Test ' + str(number),
                                'https://localhost:8443', events)
    assert isinstance(hook, Hook)


def test_get_all_hooks(fineract):
    hooks = [hook for hook in fineract.get_hooks()]
    assert len(hooks) >= 1


def test_get_single_hook(fineract):
    hooks = [hook for hook in fineract.get_hooks()]
    assert fineract.get_hooks(hooks[0].id)


def test_hook_templates(fineract):
    assert Hook.template(fineract.request_handler)


def test_hook_exists(fineract):
    assert Hook.exists(fineract.request_handler, 'Test ' + str(number))


def test_get_hook_by_name(fineract):
    assert Hook.get_by_name(fineract.request_handler, 'Test ' + str(number))


def test_get_hook_by_id(fineract):
    hook = Hook.get_by_name(fineract.request_handler, 'Test ' + str(number))
    assert Hook.get(fineract.request_handler, hook.id)


def test_hook_update(fineract):
    events = [
        {
            'actionName': 'DISBURSE',
            'entityName': 'LOAN'
        }
    ]
    hook = Hook.get_by_name(fineract.request_handler, 'Test ' + str(number))
    hook = hook.update('https://localhost:8443', events)
    assert len(hook.events) == 1
