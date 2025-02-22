<script lang="ts">
  import QuibbleTextLogo from '$lib/components/icons/logos/quibble-text.svelte';
  import QuibbleLogo from '$lib/components/icons/logos/quibble.svelte';
  import { cn } from '$lib/functions/classnames';
  import { ProfileNewSchema } from '$lib/schemas/auth';
  import type { FormProps } from '../../types';
  import forms from '../forms';
  import { defaults, superForm, type FormResult } from 'sveltekit-superforms';
  import { zod } from 'sveltekit-superforms/adapters';

  let { forms_state, update_forms_state, goto_form }: FormProps<typeof forms> = $props();

  const { form, enhance, errors, message, delayed } = superForm(defaults(zod(ProfileNewSchema)), {
    resetForm: false,
    validators: zod(ProfileNewSchema),
    onResult({ result }) {
      if (result.type === 'failure') return;
      // append to existing profiles on forms_state
      update_forms_state('profile_select', {
        profiles: [
          // @ts-expect-error: it's so obvious
          ...forms_state.profile_select.profiles,
          (result as FormResult<{ data?: { profile: object[] } }>).data?.profile
        ]
      });
      goto_form('profile_select');
    }
  });
</script>

<div class="flex flex-col gap-4">
  <!-- header section -->
  <div class="flex flex-col items-center justify-center gap-1">
    <div class="mb-3 flex items-center gap-2">
      <QuibbleLogo class="size-7" />
      <QuibbleTextLogo class="h-7 w-auto" />
    </div>
    <p class="text-center font-medium">Let's create new one!</p>
    <p class="text-center text-xs">You can edit this profile from settings page later.</p>
  </div>

  <!-- username input form section -->
  <form
    method="POST"
    action="/auth?/profile_new"
    use:enhance
    class="flex flex-col gap-3"
    novalidate
  >
    <!-- username input and errors store -->
    <div class="flex flex-col gap-1">
      <label class="input input-bordered flex items-center gap-2 bg-transparent">
        <coreicons-shape-at-sign class="size-4"></coreicons-shape-at-sign>
        <input
          type="text"
          name="username"
          class="grow border-none p-2 text-sm font-medium focus:ring-0"
          placeholder="Username*"
          bind:value={$form.username}
        />
      </label>

      <!-- superforms errors store -->
      {#if $errors.username}
        <span class="flex items-center gap-2 text-error">
          <coreicons-shape-x variant="circle" class="size-3.5"></coreicons-shape-x>
          <span class="text-xs">{$errors.username}</span>
        </span>
      {/if}
    </div>

    <!-- render message store if any or help text -->
    <div class="flex items-center gap-2" class:text-error={$message}>
      <coreicons-shape-info class="size-3.5"></coreicons-shape-info>
      <span class="text-xs">{$message ?? `Hint: Make it epic—you only get 3!`}</span>
    </div>
    <!-- with delayed store -->
    <button
      type="submit"
      class={cn($delayed && 'btn-active pointer-events-none', 'btn btn-primary')}
    >
      {#if $delayed}
        Creating
        <span class="loading loading-spinner loading-xs"></span>
      {:else}
        Create Profile
        <coreicons-shape-arrow variant="right" class="size-4"></coreicons-shape-arrow>
      {/if}
    </button>
  </form>
</div>
