<script lang="ts">
  import EighteenPlusIcon from '$lib/components/icons/18-plus.svelte';
  import { cn } from '$lib/functions/classnames';
  import type { FormProps } from '$lib/modals/types';
  import forms from '../forms';
  import { untrack } from 'svelte';

  type Type = keyof typeof type_mapping;

  let { update_forms_state, forms_state }: FormProps<typeof forms> = $props();

  let checked_mature = $state<boolean>(
    (forms_state.type as { data: { mature: boolean } }).data.mature ?? false
  );
  let checked_type = $state<Type>(
    (forms_state.type as { data: { type: Type } }).data.type ?? 'private'
  );

  const type_mapping = {
    public: {
      label: 'Public',
      description: 'Anyone can view, post, and comment to this community',
      icon: '<coreicons-shape-globe class="flex-shrink-0 size-4 md:size-5"></coreicons-shape-globe>'
    },
    restricted: {
      label: 'Restricted',
      description: 'Anyone can view, but only approved users can contribute',
      icon: '<coreicons-shape-shield variant="on" class="flex-shrink-0 size-4 md:size-5"></coreicons-shape-shield>'
    },
    private: {
      label: 'Private',
      description: 'Only approved users can view and contribute',
      icon: '<coreicons-shape-lock class="flex-shrink-0 size-4 md:size-5"></coreicons-shape-lock>'
    }
  };

  $effect(() => {
    const type = checked_type;
    const mature = checked_mature;
    untrack(() =>
      update_forms_state('type', {
        valid: true,
        data: { type, mature }
      })
    );
  });
</script>

<div class="flex flex-col gap-4">
  <!-- community type selection section -->
  <div class="flex flex-col gap-2">
    <h3 class="text-xl font-semibold text-info">Set your community type</h3>
    <p class="text-sm">
      Choose who can see and join your community. Public communities are visible in search, while
      private ones are invite-only.
    </p>
  </div>

  <!-- dynamic radio buttons for community types -->
  <div class="flex flex-col">
    {#each Object.entries(type_mapping) as [key, item]}
      {@const checked = checked_type === key}

      <div class={cn(checked && 'bg-base-200 ring-1', 'form-control rounded-xl ring-neutral')}>
        <label class="label size-full cursor-pointer gap-2 p-0 p-3">
          <div class="flex items-center gap-3">
            <!-- eslint-disable svelte/no-at-html-tags -->
            <span class:text-accent={checked}>
              {@html item.icon}
            </span>
            <div class="flex flex-col">
              <span class="label-text font-medium text-info">{item.label}</span>
              <span class="text-xs text-base-content/75">{item.description}</span>
            </div>
          </div>
          <input
            type="radio"
            name="type"
            class="radio radio-sm"
            class:radio-accent={checked}
            bind:group={checked_type}
            value={key}
          />
        </label>
      </div>
    {/each}
  </div>

  <!-- divider between sections -->
  <div class="divider my-0 h-max before:h-px after:h-px"></div>

  <!-- mature content toggle section -->
  <div class="form-control">
    <label class="label size-full cursor-pointer gap-2 p-0 p-3">
      <div class="flex items-center gap-3">
        <EighteenPlusIcon class={cn(checked_mature && 'text-accent', 'size-5')} />
        <div class="flex flex-col">
          <span class="label-text font-medium text-info">Mature (18+)</span>
          <span class="text-xs text-base-content/75">
            Users must be over 18 to view and contribute
          </span>
        </div>
      </div>
      <input
        type="checkbox"
        class="toggle toggle-accent toggle-sm rounded-box checked:!border-accent"
        bind:checked={checked_mature}
      />
    </label>
  </div>

  <!-- footer with links to policies -->
  <span class="text-sm text-base-content/75">
    By continuing, you agree to our
    <a href="/policies/moderator-code-of-conduct" class="text-base-content underline">
      Mod Code of Conduct
    </a>
    and acknowledge that you understand the
    <a href="/policies/quibble-rules" class="text-base-content underline">Quibble Rules</a>.
  </span>
</div>
