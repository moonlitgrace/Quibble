<script lang="ts">
  import { createModalsStore } from '$lib/stores/modals.svelte';
  import type { Nullable } from '$lib/types/shared';
  import forms from './forms';
  import type { FormsState, FormSubmitData, Forms } from './types';

  let _form = $state<Forms>('join');

  let current_form = $derived(forms[_form]);
  let prev_form = $state<Nullable<Forms>>(null);

  const initial_forms_state = Object.fromEntries(
    Object.keys(forms).map((key) => [key, {}])
  ) as FormsState;

  let forms_state = $state<FormsState>(initial_forms_state);

  function update_forms_state(form: Forms, data: FormSubmitData) {
    forms_state[form] = { ...forms_state[form], ...data };
  }

  function goto_form(form: Forms) {
    prev_form = _form; // add to previous form state
    _form = form;
  }

  let dialog_element = $state<Nullable<HTMLDialogElement>>(null);

  const modalsStore = createModalsStore();

  $effect(() => {
    if (modalsStore.state.get('auth')) {
      dialog_element?.showModal();
    } else {
      dialog_element?.close();
    }
  });
</script>

<dialog
  class="modal modal-bottom sm:modal-middle"
  bind:this={dialog_element}
  onclose={() => modalsStore.close('auth')}
>
  <div class="modal-box !w-[25rem]">
    {#await current_form then Form}
      <Form.default {forms_state} {update_forms_state} {goto_form} />
    {/await}
    {#if prev_form !== null}
      <div
        class="tooltip tooltip-right absolute left-2.5 top-2.5 flex"
        data-tip="Previous form"
      >
        <button
          class="btn btn-square btn-circle btn-ghost btn-sm"
          aria-label="Close modal"
          onclick={() => (_form = prev_form!)}
        >
          <coreicons-shape-arrow class="size-5" variant="left"></coreicons-shape-arrow>
        </button>
      </div>
    {/if}
    <button
      class="btn btn-square btn-circle btn-ghost btn-sm absolute right-2.5 top-2.5"
      aria-label="Close modal"
      onclick={() => dialog_element?.close()}
    >
      <coreicons-shape-x class="size-5" variant="no-border"></coreicons-shape-x>
    </button>
  </div>
  <form method="dialog" class="modal-backdrop bg-base-300/25">
    <button>close</button>
  </form>
</dialog>
